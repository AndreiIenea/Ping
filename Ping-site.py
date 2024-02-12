import subprocess

def ping_website(website):
    try:
        # Execută comanda ping către website și salvează rezultatul
        result = subprocess.run(['ping', website, '-c', '4'], capture_output=True, text=True)
        
        # Verifică dacă ping-ul a fost reușit sau nu
        if result.returncode == 0:
            print("Ping către {} a fost reușit:".format(website))
            print(result.stdout)
        else:
            print("Ping către {} a eșuat:".format(website))
            print(result.stderr)
    except Exception as e:
        print("A apărut o eroare:", e)

if __name__ == "__main__":
    website = input("Introduceți adresa website-ului pentru ping: ")
    ping_website(website)