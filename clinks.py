#count how many clinks of glasses there are per number of guests when they "cheers!"
#for example, if there are two guests there is one clink

def clinks(num_guests):
    if num_guests == 0 or num_guests == 1:
        return 0
    if num_guests == 2:
        return 1
    return num_guests - 1 + clinks(num_guests-1)

print clinks(3)
print clinks(4)
print clinks(5)
print clinks(6)
print clinks(7)
