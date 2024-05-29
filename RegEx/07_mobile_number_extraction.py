import re

def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number

if __name__ == '__main__':
    text = "ARJUN NEPALI Education Pokhara University Cosmos college of Management and technology 2019 - 2024 Computer Engineering maintaining CGPA 3.5(till 6 sem) About Me a with Computer A motivated and diligent final Engineering year student genuine enthusiasm for AI/ML. Possessing a basic AI/ML concepts, I am eager to expand my understanding through hands- on projects and coursework. knowledge of 9862569729/9813877392 nepaliarjun049@gmail.com Projects https://github.com/Arrjoon arjunnepali.infinityfreeapp.com Multivendor Ecommerce https://www.linkedin.com/in/a rjun-nepali-32b876244/ Hard Skills C,C++ python Django OOP programming Machine learning concept pandas,numpy Soft Skills Communication Positive learning attitude Teamwork Time management Web App which integrate payment gateway Khalti. manage multiple vendor and users. Customer can add to cart and place order. Vendor can create account and sell their product. vendor can see their particular own product order. [https://github.com/Arrjoon/MultiVendorEcommerceDj ango.git] Ecommerce This application based on single vendor application Searching functionality managed. Authentication and authorization handled. github link [https://github.com/Arrjoon/Ecommerce.git] Hospital Management System This application have many feature related to hospital. Doctor and patient managed. Patient can take appointment of Doctors. [https://github.com/Arrjoon/HospitalManagementSyste m.git] "
    contact_number = extract_contact_number_from_resume(text)

    if contact_number:
        print("Contact Number:", contact_number)
    else:
        print("Contact Number not found")