from csv import reader
HTML_DOCTYPE = '<!DOCTYPE html>'

def html_procedure(filename):
    procedures = open(filename)
    output = HTML_DOCTYPE
    output += '<html><ul>'

    for line in reader(procedures):
        task = line[0]
        steps = line[1:]
        output += f"<li>{task}<ol>"
        for step in steps:
            output += f"<li>{step}</li>"

        output += "</ol></li>"

    output += "</ul></html>"
    procedures.close()

    return output

print(html_procedure("man"))


a = "<!DOCTYPE html><html><ul><li>Put elephant in the fridge<ol><li>Open the fridge</li><li>Put elephant inside</li><li>Close the fridge</li></ol></li><li>Do well in COMP10001<ol><li>Listen to lectures</li><li>Attend tutorials</li><li>Do Grok worksheets</li></ol></li><li>Don't know whether to add vegetables first or rice first when cooking fried rice<ol><li>Ask mom</li><li>Do whatever mom said</li></ol></li></ul></html>"
b = "<!DOCTYPE html><html><ul><li>Put elephant in the fridge<ol><li>Open the fridge</li><li>Put elephant inside</li><li>Close the fridge</li></ol></li><li>Do well in COMP10001<ol><li>Listen to lectures</li><li>Attend tutorials</li><li>Do Grok worksheets</li></ol></li><li>Don't know whether to add vegetables first or rice first when cooking fried rice<ol><li>Ask mom</li><li>Do whatever mom said</li></ol></li></ul></html>"

print( a == b)

It is often shorter, but not particularly well-written. 1. This exact approach takes a lot of exhaustive time to go through and compare each and every permutation to the leading dog.
This could be fixed by running the code against an approximate approach, comparing on runtime and the difference in solution output accuracy,
and determine how precise the final solution must be for you. Heuristic algorithms are often more elegant in code writing but may be more complex to understand.
After evaluating all these points, choose the most efficient one depending on your priority of order.
Note: An approximate approach would explore the different configurations based on their positions in each stage and return the best performing pack from the assigned pool.


2. If the number of dogs increases to a extremely large amount of data in the code, the storage will be more inefficient during the running of such exact approach code.
A solution to this would be considering a heuristic approach/ the greedy algorithm. Potentially memoisation, divide and conquer solution if possible to save storage
could be used in order to save storage space and consequently make it run potentially quicker.



