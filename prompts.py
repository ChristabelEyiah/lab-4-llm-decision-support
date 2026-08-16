# prompts.py
# Final prompt templates for Lab 4 — LLM Decision Support
#
# Prompt evolution:
# V1 used minimal instructions.
# V2 added a specific role, factual/neutral constraints, required
# information, and a 3–4 sentence limit.
# The extraction prompt added an explicit JSON schema, a worked
# example, and instructions not to guess missing information.
# The brief prompt was designed to present evidence and red flags
# without allowing the model to make the final approve/reject decision.


SUMMARY_PROMPT = """
Summarize this loan application:

{letter_text}
"""


EXTRACT_PROMPT = """
Extract the required loan application information from the letter below.

Return ONLY a valid JSON object. Do not include markdown, explanations,
comments, or any text outside the JSON object.

The JSON object MUST contain EXACTLY these keys:

{{
  "applicant_name": "string",
  "amount_ghs": "number",
  "purpose": "string",
  "monthly_profit_ghs": "number or null",
  "has_collateral_or_guarantor": "boolean",
  "repayment_months": "number or null"
}}

Rules:
- applicant_name must be the applicant's name as stated in the letter.
- amount_ghs must be the requested loan amount in Ghana cedis.
- purpose must describe what the applicant says the loan will be used for.
- monthly_profit_ghs must be the stated monthly profit, or null if it is not stated.
- has_collateral_or_guarantor must be true if the letter states that the applicant
  has collateral or a guarantor, and false if neither is stated.
- repayment_months must be the stated repayment period in months, or null if it
  is not stated.
- If a field is not stated in the letter, use null. Do not guess.
- Use numbers for numerical values, not strings.
- Use true or false for the boolean field.

Worked example:

Letter:
"My name is Ama Osei. I run a small bakery in Accra. I am requesting
GHS 6,000 to buy an oven. My business makes GHS 1,200 profit per month.
I will repay the loan over 10 months. My brother will guarantee the loan."

Correct JSON:
{{
  "applicant_name": "Ama Osei",
  "amount_ghs": 6000,
  "purpose": "buy an oven",
  "monthly_profit_ghs": 1200,
  "has_collateral_or_guarantor": true,
  "repayment_months": 10
}}

Now extract the information from this loan application:

{letter_text}
"""


BRIEF_PROMPT = """
You are an assistant supporting a microfinance loan officer.

Based only on the information provided in the application and extracted
facts, produce a concise decision-support brief.

Identify:
- key strengths supported by evidence
- important risks or red flags supported by evidence
- missing information that would be useful for a human loan officer

Be factual, neutral, and concise. Do not invent information.
Do not make the final lending decision.
Do not say "approve" or "reject".

Application:
{letter_text}

Extracted information:
{extracted_data}
"""
