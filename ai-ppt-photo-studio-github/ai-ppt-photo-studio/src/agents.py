"""
Agent modules for AI PPT Photo Studio.

这里使用简单规则模拟多 Agent 协作逻辑。
真实项目中可以接入大语言模型、图片生成模型和 PPTX 生成库。
"""


class ResearchAgent:
    """资料理解 Agent"""

    def analyze(self, topic: str) -> str:
        return f"""
主题：{topic}

核心问题：
1. 用户制作 PPT 和图片时流程割裂
2. 排版、配图、修图耗时较长
3. AI 生成图片容易出现风格不统一和 AI 感
4. 用户需要从一个主题快速得到完整视觉方案

核心方向：
- AI PPT 自动生成
- AI 图片与照片创作
- 风格分析
- 设计评审
- 多 Agent 协作
"""


class PlanningAgent:
    """内容策划 Agent"""

    def create_ppt_plan(self, research_result: str) -> str:
        return """
PPT 页面规划：

1. 封面：智设工坊 / AI PPT Photo Studio
2. 项目背景：AI 视觉创作需求增长
3. 用户痛点：PPT、图片、修图流程割裂
4. 产品定位：AI 视觉内容创作工作台
5. 核心功能一：AI 一键生成 PPT
6. 核心功能二：AI 图片与海报生成
7. 核心功能三：照片编辑与风格统一
8. 核心功能四：AI 设计评审
9. 多 Agent 工作流
10. 使用场景
11. 产品亮点
12. 后续开发计划
"""


class VisualAgent:
    """视觉生成 Agent"""

    def generate_visual_prompt(self, topic: str) -> str:
        return f"""
视觉提示词：

AI 视觉创作软件界面概念图，主题为“{topic}”，
深色科技风 UI，中间是 PPT 编辑画布，右侧是 AI 图片生成面板，
左侧是资料管理区域，蓝紫色渐变光效，现代设计，高级感，
适合作品集展示，清晰干净，商业软件宣传风格。
"""


class ReviewAgent:
    """设计评审 Agent"""

    def review(self, plan_result: str, visual_result: str) -> str:
        return """
设计评审建议：

1. PPT 页面数量适中，适合作品集展示。
2. 建议统一使用深色科技风或极简白色科技风。
3. 页面需要突出“PPT + 图片 + 设计评审”一体化优势。
4. 视觉图不要堆太多元素，避免 AI 感。
5. 每页保留明确主标题，保证信息层级清晰。
"""
