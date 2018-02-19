import webbrowser, sys 

#address = '5500 St Louis Ave, Chicago, IL 60625'

if (len(sys.argv) > 1):
	# get address from command line
	address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/search/' + address)

#install 