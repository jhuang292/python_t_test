from stats import mean, std, remove_outliers, t_test
import math

##### MY FUNCTIONS: #####

def get_list():
    """ Lists of number values are typed in by the user """

    L = []
    while(True):
        i = raw_input()
        if i == "":
            print "Done accepting numbers."
            break
        L.append(float(i))
    return L

def print_stats(L):
    """ Display some information about the lists """

    print "Let's compute some statistics..."
    print "\tMean: %d" % mean(L)
    print "\tStandard deviation: %d" % std(L)
    print "\t# of outliers: %d" % (len(L) - len(remove_outliers(L,1)))

##### MY CODE: #####

print "Enter list 1 (float or int, press Enter to stop):"
L1 = get_list()
print "Enter list 2 (float or int, press Enter to stop):"
L2 = get_list()

# summarize data, and remove outliers
print_stats(L1)
L1 = remove_outliers(L1,1)
print_stats(L2)
L2 = remove_outliers(L2,1)

# do statistical analysis
t = t_test(L1,L2)
print "Found a t-score of %d." % t
