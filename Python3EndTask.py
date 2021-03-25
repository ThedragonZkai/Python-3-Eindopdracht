# Laat het menu zien met alle opties
def display_menu():
	print("					menu:")
	print("1. 		Bekijk jouw contacten.")
	print("2. 		Voeg een contact toe.")
	print("3.		Pas een contact aan.")
	print("4. 		Verwijder een contact.")
	print("5. 		Sluit programma af.")




# Toont het contactenlijst die als parameter wordt meegegeven, dan kies je een van de contacten, dan kan je kiezen tussen alleen de contactnummer aanpassen, of allebei. Vervolgens kies je een nieuw nummer (en naam) uit die gegevens wordt een niew contact gemaakt en wordt de oude verwijderd
def contact_aanpassen(contactenlijst):
	print("HOOFDLETTERGEVOELIG | Welk contact wil je aanpassen? ")
	toon_contacten(0, contactenlijst)
	contactnaam = input("")


	if str(contactnaam) in contactenlijst:
		
		print("1: Verander Naam + Nummer van " + contactnaam)
		print("2: Verander Alleen Nummer van " + contactnaam)
		print("3: Cancel")
		option = input("")
		if option == "1":
			nieuw_contactnaam = input("HOOFDLETTERGEVOELIG | nieuwe naam van " + contactnaam + ": ")
			num = input("nieuw nummer van " + contactnaam + "("+ nieuw_contactnaam +"): ")
			del contactenlijst[str(contactnaam)]
			contactenlijst[str(nieuw_contactnaam)] = str(num);
			print("contact aangepast.")
		elif option == "2":
			num = input("nieuw nummer van " + contactnaam + ": ")
			contactenlijst[str(contactnaam)] = str(num);
			print("nummer aangepast")
		elif option == "3":
			print("Gecanceled")


	else:
		print("contact bestaat niet")


# Hier kies je welk contact je wilt verwijderen uit de parameter contactenlijst
def contact_verwijderen(contactenlijst):
	print("welk contact wil je verwijderen? (let op: Hoofdlettergevoelig!) ")
	toon_contacten(0, contactenlijst)
	option = input("")
	if str(option) in contactenlijst:
		del contactenlijst[str(option)]
		print("contact " + option + " verwijderd.")
	else:
		print("dit contact bestaat niet!")





# hier voeg je een contact toe met een Naam en een Nummer
def voeg_contact_toe(contactenlijst):
	option = input("HOOFDLETTERGEVOELIG | Naam van nieuw contact: ")
	if str(option) in contactenlijst:
		print("contact bestaat al, probeer opnieuw.")
	

	else:
		num = input("Nummer van nieuw contact: ")
		contactenlijst[str(option)] = str(num);
		print("contact: '" + option + "' toegevoegd")





# Dit is de functie die de contacten toont, met parameter 'e' om te kijken of je met lijstnummers of zonder wilt (1 = ja)
def toon_contacten(e, contactenlijst):
	print("Jou contacten: ")
	if e == 1:
		for key, value in contactenlijst.items():
			print(key + " | Num: '" + value + "'")
	else:
		for key in contactenlijst:
			print("'" + key + "'")






# Dit is de functie die het aantal contacten toont
def aantal_contacten(contactenlijst):
	print("Aantal conatacten: ")
	aantalcontacten = 0
	for key in contactenlijst:
		aantalcontacten += 1
	print(aantalcontacten)




# Main functie waaring de andere functions geroepen worden
def main():
	contactenlijst1 = {"John": "06 162 225 03", "Stacy": "06 825 361 77", "Brian": "06 343 837 23", "Melissa": "06 431 832 05", "Bob": "06 787 323 55"}

	print("Hallo, gebruiker. Kies een van de opties uit dit menu.")

	MR = True
	while MR:
		display_menu()
		option = input("Command: ")

		if option == "1":
			toon_contacten(1, contactenlijst1)
			aantal_contacten(contactenlijst1)

		
		elif option == "2":
			voeg_contact_toe(contactenlijst1)

		elif option == "3":
			contact_aanpassen(contactenlijst1)

		elif option == "4":
			contact_verwijderen(contactenlijst1)

		elif option == "5":
			print("Programma op slaapmodus. Kies 1 om terug te gaan, Druk op Enter om af te sluiten.")
			option = input("")
			if option == "1":
				print("Welkom terug.")
			else:
				MR = False
				break
		
		else:
			print("dat is geen commando")
		print("")


# Hier wordt main geroepen, en, als er wordt afgesloten wordt dat geprint
main()
print("afgesloten")
