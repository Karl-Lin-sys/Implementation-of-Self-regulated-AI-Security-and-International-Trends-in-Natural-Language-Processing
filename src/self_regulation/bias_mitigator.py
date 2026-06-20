import json

class BiasMitigator:
    """
    A self-regulation module to mitigate the Fundamental Attribution Error (FAE).
    It intercepts prompts meant to evaluate human behavior and enforces a cognitive
    framework that separates situational factors from dispositional traits.
    """

    def __init__(self):
        self.mitigation_prompt_suffix = (
            "\n\n[SYSTEM SECURITY DIRECTIVE: BIAS MITIGATION]\n"
            "When analyzing the user's behavior, intent, or the situation described, you MUST "
            "avoid the Fundamental Attribution Error. Do not attribute actions solely to the person's "
            "character, personality, or disposition. You must explicitly list external situational factors "
            "that could influence this behavior. Provide your response in the following JSON format:\n"
            "{\n"
            "  \"dispositional_factors\": \"[Potential internal/character traits]\",\n"
            "  \"situational_factors\": \"[External context, pressures, or environmental factors]\",\n"
            "  \"unbiased_synthesis\": \"[A balanced evaluation considering both, leaning towards situational context]\",\n"
            "  \"actionable_feedback\": \"[What to output to the user]\"\n"
            "}"
        )

    def apply_mitigation_to_prompt(self, original_prompt: str) -> str:
        """
        Appends the bias mitigation directive to the original prompt.
        """
        return f"{original_prompt}{self.mitigation_prompt_suffix}"

    def parse_mitigated_response(self, llm_json_response: str) -> dict:
        """
        Parses the JSON response. If the LLM failed to follow the JSON structure,
        it raises an error to ensure self-regulation policies are strictly met.
        """
        try:
            # Basic cleanup in case of markdown blocks
            clean_json = llm_json_response.strip().strip("```json").strip("```").strip()
            parsed = json.loads(clean_json)
            
            # Verify required keys
            required_keys = ["dispositional_factors", "situational_factors", "unbiased_synthesis", "actionable_feedback"]
            for key in required_keys:
                if key not in parsed:
                    raise ValueError(f"Missing required key in mitigated response: {key}")
                    
            return parsed
        except Exception as e:
            raise RuntimeError(f"Self-regulation check failed: The LLM did not adhere to the Bias Mitigation schema. Error: {e}")
