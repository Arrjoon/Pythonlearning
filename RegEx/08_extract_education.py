import re
def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education

if __name__ == '__main__':
    text = "ARJUN NEPALI Education Pokhara University Cosmos college of Management and technology 2019 - 2024 Computer Engineering maintaining CGPA 3.5(till 6 sem) About Me a with Computer A motivated and diligent final Engineering year student genuine enthusiasm for AI/ML. Possessing a basic AI/ML concepts, I am eager to expand my understanding through hands- on projects and coursework. knowledge of 9862569729/9813877392 nepaliarjun049@gmail.com Projects https://github.com/Arrjoon arjunnepali.infinityfreeapp.com Multivendor Ecommerce https://www.linkedin.com/in/a rjun-nepali-32b876244/ Hard Skills C,C++ python Django OOP programming Machine learning concept pandas,numpy Soft Skills Communication Positive learning attitude Teamwork Time management Web App which integrate payment gateway Khalti. manage multiple vendor and users. Customer can add to cart and place order. Vendor can create account and sell their product. vendor can see their particular own product order. [https://github.com/Arrjoon/MultiVendorEcommerceDj ango.git] Ecommerce This application based on single vendor application Searching functionality managed. Authentication and authorization handled. github link [https://github.com/Arrjoon/Ecommerce.git] Hospital Management System This application have many feature related to hospital. Doctor and patient managed. Patient can take appointment of Doctors. [https://github.com/Arrjoon/HospitalManagementSyste m.git] "

    extracted_education = extract_education_from_resume(text)
    if extracted_education:
        print("Education:", extracted_education)
    else:
        print("No education information found")