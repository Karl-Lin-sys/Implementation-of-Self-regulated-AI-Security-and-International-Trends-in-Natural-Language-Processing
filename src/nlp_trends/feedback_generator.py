import json
from src.self_regulation.bias_mitigator import BiasMitigator

class FeedbackGenerator:
    """
    A module demonstrating the NLP trend of AI-Based Natural Language Feedback,
    as evidenced by the 2026 RCT: 'Effect of AI-Based Natural Language Feedback 
    on Engagement and Clinical Outcomes in Fully Self-Guided Internet-Based CBT...'.
    
    This module strictly uses the BiasMitigator to avoid the Fundamental Attribution Error
    when generating feedback about human behavior or progress.
    """

    def __init__(self, mitigator: BiasMitigator):
        self.mitigator = mitigator

    def simulate_llm_evaluation(self, user_behavior_log: str) -> str:
        """
        Simulates the LLM processing the behavior log and generating the JSON
        structure enforced by the BiasMitigator.
        """
        # Mocking an LLM generating the structured response
        if "missed login" in user_behavior_log.lower():
            return json.dumps({
                "dispositional_factors": "User might be perceived as unmotivated, lazy, or disengaged.",
                "situational_factors": "User had a heavy workload this week, experienced a family emergency, or encountered technical issues with the internet.",
                "unbiased_synthesis": "While the user missed their logins, this is highly likely due to external stressors or scheduling conflicts rather than a lack of commitment.",
                "actionable_feedback": "We noticed you haven't logged in recently. We know life can get overwhelmingly busy! Whenever you're ready, we're here to help you pick up where you left off."
            })
        elif "completed exercise" in user_behavior_log.lower():
            return json.dumps({
                "dispositional_factors": "User is highly motivated, diligent, and disciplined.",
                "situational_factors": "User had a supportive environment this week and the app reminders were timed well.",
                "unbiased_synthesis": "The user's completion of the exercise reflects both personal effort and a conducive environment that allowed them to focus.",
                "actionable_feedback": "Great job completing your exercise! It looks like you found a good time and space to focus. Keep up this momentum!"
            })
        else:
             return json.dumps({
                "dispositional_factors": "Unknown traits.",
                "situational_factors": "Unknown environment.",
                "unbiased_synthesis": "Behavior must be evaluated in context.",
                "actionable_feedback": "Thank you for using the platform. Let us know how we can support your journey."
            })

    def generate_feedback(self, user_behavior_log: str) -> str:
        """
        Generates feedback safely by passing the context through the bias mitigator.
        """
        prompt = f"Analyze the following user log and provide supportive CBT feedback: '{user_behavior_log}'"
        
        # 1. Self-regulation: Apply the bias mitigation directive to the prompt
        mitigated_prompt = self.mitigator.apply_mitigation_to_prompt(prompt)
        
        # 2. Get LLM response (Simulated)
        llm_response = self.simulate_llm_evaluation(user_behavior_log)
        
        # 3. Self-regulation: Parse and verify the response adhered to the mitigation
        verified_data = self.mitigator.parse_mitigated_response(llm_response)
        
        # Return only the safe, actionable feedback to the user
        return verified_data["actionable_feedback"]
