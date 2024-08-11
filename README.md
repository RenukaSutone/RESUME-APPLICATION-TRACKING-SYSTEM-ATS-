# 📄 ATS Tracking System

Welcome to the **ATS Tracking System**! This tool is designed to assist HR professionals and recruiters in reviewing resumes and evaluating their alignment with job descriptions. The system leverages the power of the **Gemini-1.5-Flash** generative model from Google's Generative AI library to generate content based on the input provided.

## 🚀 Introduction

The **ATS Tracking System** automates the resume review process by using advanced AI to compare resumes against job descriptions. By doing so, it helps recruiters quickly identify the most suitable candidates for a position, saving time and improving the accuracy of the hiring process.

## 🧠 Key Concepts

- **ATS (Applicant Tracking System)**: An automated system used by HR professionals and recruiters to manage and track job applications and resumes.
- **Gemini-1.5-Flash**: A generative model developed by Google's Generative AI library that generates content based on given inputs, aiding in the analysis of resumes.
- **PDF to Image Conversion**: The system converts uploaded PDF resumes into images for processing and analysis.
- **Percentage Match**: The system calculates the percentage match between a resume and a job description, indicating how well the resume aligns with the job's requirements.

## 🗂️ Code Structure

The codebase is organized to facilitate the conversion of resumes to analyzable formats, interact with the generative AI model, and provide user-friendly interfaces via Streamlit. Below is an overview of the main components:

1. **Import necessary libraries and modules**:
   - `dotenv`: Loads environment variables.
   - `base64`: Encodes and decodes base64 data.
   - `streamlit`: Creates the Streamlit app interface.
   - `os`: Accesses environment variables and configures the generative AI library.
   - `io`: Handles file input/output.
   - `PIL`: Processes images.
   - `pdf2image`: Converts PDF files to images.
   - `google.generativeai`: Configures and utilizes the generative AI model.

2. **Define the `get_gemini_response` function**:
   - Accepts three inputs: `input`, `pdf_content`, and `prompt`.
   - Configures the generative model with the specified version.
   - Generates content based on the provided inputs and returns the response.

3. **Define the `input_pdf_setup` function**:
   - Accepts an uploaded file as input.
   - If the file is a PDF, converts it to an image using the `pdf2image` library.
   - Converts the image to bytes and encodes it in base64 format.
   - Returns the encoded image data.

4. **Create the Streamlit app**:
   - Sets page configuration and displays the header.
   - Provides input fields for the job description and resume upload.
   - Handles user interactions with buttons.
   - Defines input prompts for different scenarios.
   - Calls the `input_pdf_setup` function to convert the uploaded PDF to image data.
   - Calls the `get_gemini_response` function to generate content based on the inputs.
   - Displays the generated response.

## 🎯 Conclusion
The ATS Tracking System is a powerful tool that leverages generative AI to analyze resumes and evaluate their alignment with job descriptions. By utilizing the Gemini-1.5-Flash model, the system generates content based on the provided inputs, allowing HR professionals and recruiters to make informed decisions. With the ability to convert PDF resumes to images and calculate the percentage match, this system streamlines the resume review process and enhances the efficiency of talent acquisition.
