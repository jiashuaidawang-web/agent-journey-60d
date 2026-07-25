# Day 33 Boss 答案

## 1. Agent 系统有哪些安全风险？

| 风险 | 说明 | 危害 |
|------|------|------|
| Prompt Injection | 恶意用户注入指令 | 执行恶意操作 |
| Data Leakage | 敏感数据泄露 | 数据泄露 |
| Tool Permission | 工具权限过大 | 越权操作 |
| Agent Permission | Agent 权限控制 | 未授权访问 |
| Denial of Service | 大量请求 | 服务不可用 |

## 2. 如何防护 Prompt Injection？

**防护策略**：
1. **输入校验**：检测恶意模式
2. **System Prompt 保护**：不允许用户修改
3. **输出过滤**：过滤敏感信息
4. **权限控制**：限制 Agent 权限
5. **审计日志**：记录所有操作

## 3. 如何实现 Tool Permission 控制？

**实现方式**：
1. **Tool Registry**：注册时定义权限
2. **Permission Check**：调用前检查权限
3. **Role-Based Access**：基于角色的访问控制
4. **Audit Log**：记录工具调用
