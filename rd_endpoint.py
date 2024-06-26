import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
from pprint import pprint

#input_text = """Questionnaire and Response   Name:Oghenekaro Rachael Ojoh   Date of Birth: 31st May 1982   Marital Status:Single   Product Type:EEP/PNP   IELTS scores for Principal applicant: Listening- 8.5, Reading-8.0, Speaking-7.5,  and Writing-7.5 (Projected)   IELTS scores for Dependent spouse: Listening-, Reading-, Speaking-, and  Writing-None   Available degrees for Principal applicant: Secondary school certificate and or/  OND (Ordinary National diploma) HND (Higher National Diploma), Bachelor\'s  degree, Post graduate Diploma, Masters degree, PHD (Doctorate): Diploma and  Bachelors degree.   Available degrees for Dependent spouse: Secondary school certificate and or/  OND (Ordinary National diploma) HND (Higher National Diploma), Bachelor\'s  degree, Post graduate Diploma, Masters degree, PHD (Doctorate): None   Years of work experience for Principal applicant:3 years and more.   Have you had a previous Canada visa application? If yes, how many?:None   Details of Previous Canada visa application:(date/month/year, start and end date  he academic qualification that was was filled, start and end dates off all work  experience filled )None   Do you have family members who reside in Canada as permanent residence? If  yes, specify your relationship with them and the province in which they  reside.None"""


def multiturn_generate_content(input_text):
  vertexai.init(project="247572588539", location="us-central1")
  model = GenerativeModel(
    "projects/247572588539/locations/us-central1/endpoints/1135626186701930496",
    system_instruction=[system_prompt]
  )
  response = model.generate_content(contents=[input_text],generation_config=generation_config,stream=True)
  return response


system_prompt = """You are a visa advisor with expertise in tailoring personalized roadmaps for clients navigating the visa application process. Based on a client\'s profile, including demographics, educational background, work experience, and target destination, generate a comprehensive roadmap that outlines: Client Information: Name, Age, Country of Origin Visa Product: Specific visa program (e.g., Canada Express Entry, Ontario PNP) Eligibility Assessment: Analyze client\'s profile against program requirements. Identify any gaps (e.g., education evaluation, language tests)  Recommended Pathways: Suggest multiple visa options with justifications based on client\'s strengths and program requirements.  National Occupation Classification (NOC) Selection: Recommend relevant NOC codes aligned with client\'s experience and program eligibility. Explain the rationale behind each suggestion.  Required Documents: Generate a detailed list of documents required for the application, including:  Standardized test scores (e.g., IELTS, TEF) with minimum score requirements for each skill (reading, writing, listening, speaking)  Educational credentials and evaluation reports (if needed)  Employment documents (reference letters, job offer, payslips) for work experience NOCs  Proof of funds or sponsorship documents (if applicable)  Timeline with Milestones: Outline a realistic timeline with key milestones for each stage of the application process, including:  Eligibility Requirements Completion (Month): Credential evaluation, language test completion, NOC selection.  Pre-ITA Stage (Month): Profile creation, review, and submission.  ITA and Documentation (Month): Document review, post-ITA profile completion and submission.  Biometric Request (Month): Biometrics completion.  Passport Request (PPR) (Month): Document submission and processing.  Confirmation of Permanent Residency (COPR) (Month): Visa approval and passport return.  Note: Mention potential delays due to third-party processing times (e.g., credential evaluation, provincial processing).  Additional Considerations: Include relevant information for specific program pathways (e.g., PNP - provincial nomination requirements).  Transparency and Disclaimers: Acknowledge limitations in controlling processing times.  Client-Specific Notes: Add personalized comments based on the client\'s profile, like highlighting strengths or addressing weaknesses."""

generation_config = {
    "max_output_tokens": 1200,
    "temperature": 1,
    "top_p": 1
    
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}
"""
response=multiturn_generate_content(input_text)
for chunk in response:
  # Process each chunk of generated text
  print(chunk.text)
"""

