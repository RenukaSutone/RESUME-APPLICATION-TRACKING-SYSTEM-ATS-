from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager with a deep understanding of the requirements 
 for various technical roles, including data science, software engineering, and analytics. Your task is to thoroughly review the provided resume against the job description provided below. Please perform the following:
1. Evaluate the candidate's qualifications, skills, and experiences in relation to the job description.
2. Identify and highlight the strengths and weaknesses of the applicant's profile.
3. Provide detailed feedback on how well the candidate aligns with the specified job requirements.
4. Suggest any areas of improvement or additional skills that could enhance the candidate's suitability for the role.
5. Rate the overall fit of the candidate for the role on a scale of 1 to 10.
Your professional evaluation should be precise, insightful, and based on your expertise in technical recruitment.
"""

input_prompt2 = """
You are a seasoned career coach and industry expert in data science and software engineering. 
Your task is to analyze the provided resume and the job description to offer constructive feedback 
on how the candidate can improve their skills to better match the job requirements. Please perform the following:
1. Review the candidate's current skills and experiences as listed in the resume.
2. Compare the candidate's profile with the job description to identify any gaps in skills or experiences.
3. Provide specific recommendations on the skills, certifications, or experiences the candidate should acquire to increase their chances of securing the desired role.
4. Suggest relevant courses, training programs, or projects that could help the candidate bridge the identified skill gaps.
5. Offer general advice on career progression and skill development in the field of data science and software engineering.
Your guidance should be actionable, detailed, and tailored to the candidate's career growth in the technical domain.
"""

input_prompt3 = """
You are a skilled Applicant Tracking System (ATS) scanner with a deep understanding of the functionality and requirements 
of ATS systems used in the hiring process for technical roles. Your task is to evaluate the provided resume against the job description and provide a comprehensive report.
 Please perform the following:
1. Calculate the percentage match between the resume and the job description based on keywords and relevant experiences.
2. Identify and list the key skills, qualifications, and experiences mentioned in the job description that are missing in the resume.
3. Provide a detailed summary of how well the resume aligns with the job requirements, including both strengths and areas of improvement.
4. Offer suggestions on how the candidate can optimize their resume to improve the match percentage and enhance visibility in ATS systems.
Your evaluation should be precise, data-driven, and provide actionable insights to help the candidate improve their resume's performance in ATS systems.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")



   




