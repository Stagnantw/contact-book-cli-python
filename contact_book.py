import re
class ContactBook:
  def __init__(self,filename="contact.txt"):
    self.filename=filename
  def add_contact(self):
    print("-------Welcome to the contact book-------")
    name=input("Enter name: ")
    while True:
      phone_number=input("Enter phone number:")
      if phone_number.isdigit() and len(phone_number) == 11:
        break
      else:
        print("❌ Invalid phone number. Must be 11 digits.")
    while True:
      email=input("Enter email id: ")
      if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        break
      else:
        print("❌ Invalid email format. Try again (e.g., example@email.com)")
    try:
      with open(self.filename,"a") as f:
        f.write("====================\n")
        f.write(f"Name:{name}\n")
        f.write(f"Phone_number:{phone_number}\n")
        f.write(f"Email:{email}\n")
        f.write("====================\n")
    except Exception as e:
      print(f"Error saving contact :{e}")
  def search_contact(self,field):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return 
    value=input(f"Enter the {field.lower()} to search contact: ").strip()
    pattern = rf"^{re.escape(field)}:\s*{re.escape(value)}"
    found=False
    for i,line in enumerate(lines):
      if re.search(pattern,line,re.IGNORECASE):
        for j in range(i-1,i+5):
          if 0<=j<len(lines):
            print(lines[j].strip())
        found=True
        break
    if not found:
      print(f"No contact found with that {field.lower()}.")
  def delete_contact(self,field):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return
    value=input(f"Enter the {field.lower()} to delete contact: ").strip()
    pattern = rf"^{re.escape(field)}:\s*{re.escape(value)}"
    new_lines=[]
    found=False
    i=0
    while i < len(lines):
      line=lines[i]
      if re.search(pattern,line,re.IGNORECASE):
        found=True
        while i > 0 and not lines[i-1].startswith("===================="):
          i-=1
        while i < len(lines) and not lines[i].startswith("===================="):
          i+=1
        if i < len(lines):
          i+=1
      else:
        new_lines.append(line)
        i+=1
    if found:
      with open(self.filename,"w") as f:
        f.write("".join(new_lines))
      print("Contact deleted successfully")
    else:
      print(f"No contact found with that {field.lower()}.")
  def edit_contact(self,field):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found")
      return
    value=input(f"Enter {field.lower()}  to edit: ").strip()
    pattern = rf"^{re.escape(field)}:\s*{re.escape(value)}"
    new_lines=[]
    found=False
    i=0
    while i < len(lines):
      line=lines[i]
      if re.search(pattern,line,re.IGNORECASE):
        found=True
        while i > 0 and not lines[i-1].startswith("===================="):
          i-=1
        while i < len(lines) and not lines[i].startswith("===================="):
          i+=1
        if i < len(lines):
          i+=1 
        
        new_name=input("Enter name: ")
        while True:
          new_phone_number=input("Enter phone_number: ")
          if new_phone_number.isdigit() and len(new_phone_number) == 11:
            break
          else:
             print("❌ Invalid phone number. Must be 11 digits.")
        while True:
          new_email=input("Enter email: ")
          if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', new_email):
            break
          else:
             print("❌ Invalid email format. Try again (e.g., example@email.com)")
        new_lines.append("====================\n")
        new_lines.append(f"Name:{new_name}\n")
        new_lines.append(f"Phone_number:{new_phone_number}\n")
        new_lines.append(f"Email:{new_email}\n")
        new_lines.append("====================\n")
      else:
        new_lines.append(line)
        i+=1
    if found:
      with open(self.filename,"w") as f:
        f.write("".join(new_lines))
      print("Contact update successfully")
    else:
      print(f"No contact found with that {field.lower()}.")
  def list_all_names(self):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
        names=[line.strip().replace("Name:","")for line in lines if line.startswith("Name:")]
        if names:
          print("All Saved Names\n")
          for idx,name in enumerate(names,1):
            print(f"{idx}.{name}")
        else:
          print("No name found")
    except FileNotFoundError:
      print("No file found")
  def print_all_contact_info(self):
    try:
      with open(self.filename,"r") as f:
        content=f.read().strip()
        parts=re.findall(r"=+\n(.*?)\n=+",content,re.DOTALL)
        if parts:
          print("\nAll saved contact info\n")
          for idx,part in enumerate(parts,1):
            print(f"Contact:{idx}\n")
            print(part.strip())
        else:
          print("No contact found")
    except FileNotFoundError:
      print("No file found")

obj=ContactBook()

while True:
  print("\n---Contact Book Menu---")
  print("1.Add contact")
  print("2.Search contact")
  print("3.Delete contact")
  print("4.Edit contact")
  print("5.List All names")
  print("6.Print All contact info")
  print("7.Exit")

  choice=input("Enter your choice (1-7):")

  if choice == "1":
    obj.add_contact()
  elif choice == "2":
    field=input("Enter Search by (Name/Phone_number/Email): ").strip()
    obj.search_contact(field)
  elif choice == "3":
    field=input("Enter Delete by (Name/Phone_number/Email: )").strip()
    obj.delete_contact(field)
  elif choice == "4":
    field=input("Enter edit by (Name/Phone_number/Email): ").strip()
    obj.edit_contact(field)
  elif choice == "5":
    obj.list_all_names()
  elif choice == "6":
    obj.print_all_contact_info()
  elif choice == "7":
    print("Exiting contact Book.Goodbye!")
    break
  else:
    print("Invalid choice!Please try again")