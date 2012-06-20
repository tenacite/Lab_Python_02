theInput = raw_input("Enter an integer: ")
i = theInput
i = int(i)
if i%2==0:
    print 'even'
else:
    print 'odd'
print '------------------------'
primarySchoolAge= 5
legalVotingAge= 18
ageForPresidency= 45
retirementAge=60
personsAge=input("Enter an age: ")
if personsAge<primarySchoolAge:
    print "too young"
elif personsAge<ageForPresidency:
    print "You can't be president"
elif personsAge>=legalVotingAge:
    print "Remember to vote"
elif personsAge>=retirementAge:
    print "Too Old"
elif personsAge>=ageForPresidency:
    print "Vote for me"

print"-----------------------------"
for i in range(40,-1,-1):
    if i%3 == 0:
         print i
print"-----------------------------"
