"""
AI PPT Photo Studio - Demo Entry

这是一个概念项目的简单命令行示例。
后续可以扩展为 Web 应用、桌面软件或插件工具。
"""

from agents import ResearchAgent, PlanningAgent, VisualAgent, ReviewAgent


def main():
    topic = "AI 制作 PPT 与照片的软件"

    research_agent = ResearchAgent()
    planning_agent = PlanningAgent()
    visual_agent = VisualAgent()
    review_agent = ReviewAgent()

    research_result = research_agent.analyze(topic)
    plan_result = planning_agent.create_ppt_plan(research_result)
    visual_result = visual_agent.generate_visual_prompt(topic)
    review_result = review_agent.review(plan_result, visual_result)

    print("=== 资料理解结果 ===")
    print(research_result)

    print("\n=== PPT 策划结果 ===")
    print(plan_result)

    print("\n=== 视觉提示词 ===")
    print(visual_result)

    print("\n=== 设计评审 ===")
    print(review_result)


if __name__ == "__main__":
    main()
