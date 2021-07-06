""" S3JulQ01

The captains.txt file that I used as data is present at : https://github.com/asarfraaz/PyPractice/blob/master/data/captains.txt

Few questions that you can try solving based on captains.txt file are as follows :

1> Print the first 5 lines of captains.txt
2> Print the last 5 lines of captains.txt

3> Print only the first 5 captain names from captains.txt [ Note : 'Player' is not a name of captain ]
4> Print the Span and Player name for all players in captains.txt

5> For every captain in captains.txt, display the Player Name, Matched played, Matches Won and Matches Lost
6> Display the above information, sorting by Player Name
7> Display information of question 5, sorting by Matches played
8> Display information of question 5, sorting by Matches won, showing the captain with the highest wins on top
9> Display information of question 5, sorting by Matches lost, showing the captain with the most losses at the bottom

10> Using the dictionary created in question 5, find the "win percentage" for each captain [ Matches Won divided by Matches Played ] and display this information along with the details mentioned in question 5

11> Display the information in question 10, showing the captains with the highest win percentage on top
12> Display the same information as in question 11, but discard the players who have played 5 or less matches.

13> Who are the top 5 captains that have captained India for the most number of years ?

This last one is very lengthy and quite difficult. You can do it at your leisure
14> Which years did India have more than 3 captains ?

Input File: Captains.txt

"""
def get_filename_as_agrv_and_get_filehandle():
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    opened = False
    arglen = len(sys.argv)
    while not opened:
        if arglen < 2:
            file = input( "Enter Data Filename with text contents:")
        else:
            file = sys.argv[1]
        try:
            RFH = open(file)
            opened = True
        except FileNotFoundError:
            print("File Not Found!!")
            arglen = 1 # forcing to collect file name, if argument file name was wrong.
    return  RFH

def process_line(line,captain_data):
    parts = list()
    parts = line.split(',')
#    print(parts)
    captain_data[parts[0]] = parts[1:]
    return captain_data

def get_match(x):
    return int(captain_data[x][1])
def get_match_won(x):
    return int(captain_data[x][2])
def get_match_lost(x):
    return int(captain_data[x][3])
def get_percent_based_ZtoA(x):
    return captain_data[x][7]
def cal_noff(span):
    years = span.split('-')
    return int(years[1])-int(years[0])+1

def get_noff_years(x):
    return captain_data[x][8]

def get_year_range(span):
    years = span.split('-')
    return int(years[0]),int(years[1])

import sys


# Main starts here
if __name__ == "__main__":

    #Getting File read & Building a Dictionary
    RFH = get_filename_as_agrv_and_get_filehandle()
    headings = next(RFH)
    captain_data =dict()
    lines = list()
    while True:
        try:
            line = next(RFH)
#            print(line)
            captain_data = process_line(line[0:len(line)-1],captain_data)
            lines.append(line[0:len(line)-1])
        except StopIteration:
            break;
    RFH.close()
#    print(lines)
#    print("Dictionary:-",captain_data)
    print("#1 First 5 lines:-\n")
    print(headings,end = "")
    for i in range(0,4):
        print(lines[i])
    print ("\n#2 Last 5 lines:-\n")
    for i in range(len(lines)-1,len(lines)-6,-1):
        print(lines[i])
    print ('\n#3 First 5 Captain Names:-\n')
    for i in range(0,5):
        c = list(captain_data)[i]
        print(f'{i+1:>3d}.  {c!s:<25}')
    print ('\n#4 Span and Player Names for all players:-\n')
    print(f'\n{"Span"!s:<10}  {"Player Name"!s:<25}')
    for i in range(0,len(captain_data)):
        c = list(captain_data)[i]
        sp = captain_data[c][0]
        print(f'{sp!s:<10}  {c!s:<25}')
    print(f'\n{"#5. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)":^88}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20}\n')
    for c in captain_data:
        mp = captain_data[c][1]
        mw = captain_data[c][2]
        ml = captain_data[c][3]
        print(f'{c:>25} {mp:^20} {mw:^20} {ml:^20}')
    print(f'\n{"#6. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- Alphabetical Order":^85}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20}')
    for plyr in sorted(captain_data):
        print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20}')
    print(f'\n{"#7. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- Sorted on Matches PLayed":^85}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20}')
    for plyr in sorted(captain_data,key=get_match):
        print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20}')
    print(f'\n{"#8. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- Sorted on Matches Won":^85}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20}')
    for plyr in sorted(captain_data,key=get_match_won,reverse=True):
        print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20}')
    print(f'\n{"#9. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- Sorted on Matches Lost":^85}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20}')
    for plyr in sorted(captain_data,key=get_match_lost):
        print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20}')
    for each in captain_data:
        items = captain_data.get(each)
        items.append(int(items[2])/int(items[1]))
        captain_data[each] = items
    print(f'\n{"#10. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)":^98}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20} {"Win Percentage":^15}\n')
    for plyr in captain_data:
        print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20} {captain_data[plyr][7]:>10.2%} ')
    print(f'\n{"#11. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- SORTED ON WIN PERCENTAGE":^98}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20} {"Win Percentage":^15}\n')
    for plyr in sorted(captain_data,key=get_percent_based_ZtoA,reverse=True):
            print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20} {captain_data[plyr][7]:>10.2%} ')
    print(f'\n{"#12. PLAYER V/S MATCHS(PLAYED, WON & LOST INFORMATION)- SORTED ON WIN PERCENTAGE":^98}')
    print(f'{"(Only players who played more than 5 matches)":^98}\n')
    print(f'{"Payer Name"!s:>25} {"MatchesPlayed":^20} {"Matches Won":^20} {"Matches Lost":^20} {"Win Percentage":^15}\n')
    for plyr in sorted(captain_data,key=get_percent_based_ZtoA,reverse=True):
        if int(captain_data[plyr][1]) > 5:
            print(f'{plyr:>25} {captain_data[plyr][1]:^20} {captain_data[plyr][2]:^20} {captain_data[plyr][3]:^20} {captain_data[plyr][7]:>10.2%} ')
    count = 0
    for each in captain_data:
        noff = cal_noff(captain_data[each][0])
        items = captain_data.get(each)
        items.append(noff)
        captain_data[each] = items
    print(f'\n{"#13. TOP 5 CAPTAINS captained India for Most number of years":^60}\n')
    print(f'{"#  Captain Name"!s:<20} {"No of Years":<15}')
    for plyr in sorted(captain_data,key=get_noff_years,reverse=True):
        if count < 5:
            print(f'{count+1:<1d}. {plyr:<20}{captain_data[plyr][8]:>4d} ')
            count+= 1
        
#Making a dictionary of the data
    print(f'\n{"#14. YEARS INDIA HAD MORE THAN 3 CAPTAINS"}\n')
    print(f'{"Year"!s:^6}{"No.of Captions":^20}\n')
#Building list of Years in Data
    years = list()
    for each in captain_data:
        st,end = get_year_range(captain_data[each][0])
        for y in range(st,end+1):
            if y not in years:
                years.append(y)
    years = sorted(years)
    captain_count = list()
    for i in range(0,len(years)):
        captain_count.append(0)
        
    for each in captain_data:
        st,end = get_year_range(captain_data[each][0])
        for y in range(st,end+1):
            if y in years:
                i = years.index(y)
                captain_count[i] += 1
    for i in range(0,len(years)):
        if captain_count[i] > 3:
            print (f'{years[i]:^6}{captain_count[i]:^20}')

         
                                
