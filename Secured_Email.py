def secured_emails(input):
    index=input.find('@')
    domain=input[index:]
    a=input[0]+('*')*index+domain
    return a

print(secured_emails('mohdtoufique28786@gmail.com'))