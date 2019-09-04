firstName = "Joel"
middleName = "Teodor"
lastName = "Nilsson"
nickName = "Timings"
domän = "ntig"
#print(firstName[3])

tecken = """paranteser(),
hakparanteser[],
måsvingar{},
kolon:,
semikolon;, 
komma, \" dubbelfnutt, \' enkelfnutt"""

userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"
#print(userName)

skolmail = firstName.lower()
skolmail += "."
skolmail += lastName.lower()
skolmail += "@elev.ga."
skolmail += domän.lower()
skolmail += ".se"

print(skolmail)