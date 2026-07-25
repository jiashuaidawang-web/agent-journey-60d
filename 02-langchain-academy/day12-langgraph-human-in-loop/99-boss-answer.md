# Day 12 Boss 答案

## 1. interrupt 和 Checkpoint 的关系？

**关系**：
- interrupt 依赖 Checkpoint 机制
- 当 Graph 在 interrupt 点暂停时，当前 State 被保存到 Checkpoint
- 恢复执行时，从 Checkpoint 读取 State 继续

**流程**：
```
Graph 执行到 interrupt 节点
    ↓
当前 State 保存到 Checkpoint
    ↓
Graph 暂停，控制权返回给调用方
    ↓
调用方获取人工输入
    ↓
调用方更新 State（可选）
    ↓
调用 app.invoke(None, config) 恢复执行
    ↓
从 Checkpoint 读取 State，继续执行
```

## 2. 什么场景需要 Human-in-the-loop？

**典型场景**：

1. **高风险操作**：
   - 删除文件、发送邮件、执行支付
   - 需要人工确认后才能执行

2. **关键决策点**：
   - Agent 生成的方案需要审批
   - 重要业务决策需要人工确认

3. **异常处理**：
   - Agent 遇到无法处理的情况
   - 需要人工介入判断

4. **质量控制**：
   - Agent 输出需要人工审核
   - 确保输出符合要求

5. **合规要求**：
   - 某些操作必须有审批记录
   - 满足审计要求

## 3. 如何实现审批通过/拒绝的不同处理？

**通过条件边实现**：

```python
def route_approval(state: State):
    if state.get("approved"):
        return "execute"    # 审批通过 → 执行
    return "reject"         # 审批拒绝 → 拒绝处理

graph.add_conditional_edges("approval", route_approval, {
    "execute": "execute_node",
    "reject": "reject_node",
})
```

**完整流程**：
```
Agent 生成方案
    ↓
暂停，等待人工审批
    ↓
人工输入：通过/拒绝
    ↓
更新 State：approved = True/False
    ↓
条件边根据 approved 决定走向
    ↓
通过 → 执行节点
拒绝 → 拒绝节点
```
