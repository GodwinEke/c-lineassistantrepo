"""
Author: Godwin Chierika Eke
Email: https://mailto:ekegodwinc@gmail.com
Github: https://githubcom/GodwinEke

"""
import time

def formatted(word) -> str:
    return word.strip().lower()

def is_state(state):
        """
        Assumes state as str,
        Lowers state into lowercase,
        Returns state if state input matches a state in list of USA states
        Returns None if state does not match any state in list of USA states
        """

        # remove all trailing whitespaces if there is
        lower_state = formatted(state)
        USA_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
                      'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky',
                      'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri',
                      'montana', 'nebraska', 'nevada', 'new hamsphire', 'new jersey', 'new mexico', 'new york', 'north carolina',
                      'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode_island', 'south carolina', 'south dakota',
                      'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virigina', 'wisconsin', 'wyoming']

        if lower_state in USA_states:
            return lower_state

        return None

def is_license(license):
        """
        Assumes license as str,
        Returns dict if license matches the name of the dict
        Returns None if license does not match any dict
        """

        # Types of licenses (Data was retrived from the world population review)
        # 1
        full_license = {'alabama': 17, 'alaska': 16.5, 'arizona': 16.5, 'arkansas': 18, 'california': 17, 'colorado': 17,
                        'connecticut': 18, 'delaware': 17, 'florida': 18, 'georgia': 18, 'hawaii': 17, 'idaho': 16,
                        'illinois': 18, 'indiana': 18, 'iowa': 17, 'kansas': 16.5, 'kentucky': 17, 'louisiana': 17, 'maine': 16.75,
                        'maryland': 18, 'massachusetts': 18, 'michigan': 17, 'minnesota': 16.5, 'mississippi': 16.5, 'missouri': 17.92,
                        'montana': 16, 'nebraska': 17, 'nevada': 16.5,  'new hamsphire': 16.5, 'new jersey': 18, 'new mexico': 16.5,
                        'new york': 17, 'north carolina': 16.5, 'north dakota': 16, 'ohio': 18, 'oklahoma': 16.5, 'oregon': 17,
                        'pennsylvania': 17, 'rhode island': 17.5, 'south carolina': 16.5, 'south dakota': 16, 'tennessee': 17,
                        'texas': 18, 'utah': 17, 'vermont': 18, 'virginia': 18, 'washington': 18, 'west virigina': 17, 'wisonsin': 16.75, 'wyoming': 16.5}

        # 2
        provisional_license = {'alabama': 16, 'alaska': 16, 'arizona': 16, 'arkansas': 16, 'california': 16, 'colorado': 16,
                               'connecticut': 16.33, 'delaware': 16.5, 'florida': 16.515, 'georgia': 16, 'hawaii': 16, 'idaho': 15,
                               'illinois': 16, 'indiana': 16.25, 'iowa': 16, 'kansas': 16, 'kentucky': 16.5, 'louisiana': 16, 'maine': 16,
                               'maryland': 16.5, 'massachusetts': 16.5, 'michigan': 16, 'minnesota': 16, 'mississippi': 16, 'missouri': 16,
                               'montana': 15, 'nebraska': 16, 'nevada': 16,  'new hamsphire': 16, 'new jersey': 17, 'new mexico': 15.5,
                               'new york': 16.5, 'north carolina': 16, 'north dakota': 16, 'ohio': 16, 'oklahoma': 16, 'oregon': 16,
                               'pennsylvania': 16.5, 'rhode island': 16.5, 'south carolina': 15.5, 'south dakota': 14.5, 'tennessee': 16,
                               'texas': 16, 'utah': 16, 'vermont': 16, 'virginia': 16.25, 'washington': 16, 'west virigina': 16, 'wisonsin': 16, 'wyoming': 16}

        # 3
        learner_permit = {'alabama': 15, 'alaska': 14, 'arizona': 15.5, 'arkansas': 14, 'california': 15.5, 'colorado': 15,
                          'connecticut': 16, 'delaware': 16, 'florida': 15, 'georgia': 15, 'hawaii': 15.5, 'idaho': 14.5, 'illinois': 15, 'indiana': 15,
                          'iowa': 14, 'kansas': 14, 'kentucky': 16, 'louisiana': 15, 'maine': 15, 'maryland': 15.75, 'massachusetts': 16, 'michigan': 14.75,
                          'minnesota': 15, 'mississippi': 15, 'missouri': 15, 'montana': 14.5, 'nebraska': 15, 'nevada': 15.5,  'new hamsphire': 15.5,
                          'new jersey': 16, 'new mexico': 15, 'new york': 16, 'north carolina': 15, 'north dakota': 14, 'ohio': 15.5, 'oklahoma': 15.5, 'oregon': 15,
                          'pennsylvania': 16, 'rhode island': 16, 'south carolina': 15, 'south dakota': 14, 'tennessee': 15, 'texas': 15, 'utah': 15, 'vermont': 15,
                          'virginia': 15.5, 'washington': 15, 'west virigina': 15, 'wisonsin': 15.5, 'wyoming': 15}

        # return license according to user input
        if license == 'a' or license == 'full' or license == 'full license':
            return provisional_license
        elif license == 'b' or license == 'provisional' or license == 'provisional license' or license == 'provisionallicense':
            return full_license
        elif license == 'c' or license == "learner's permit" or license == 'learners permit' or license == 'learnerspermit':
            return learner_permit
        return None


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


# verify eligibility
def Eligibility(state, license, age) -> str:
    """
    Assumes state and license as str, age as int,
    returns a congratulatory message if eligible for license inputted if age >=min_age for license
    returns an ineligibility message if NOT eligible for license inputted <min_age for license
    """

    state = is_state(state)
    license = is_license(license)
    if age >= license[state]:
        return "\nCongratulations, you are eligible! :)\n"
    else:
        return "\nSorry, you are not eligible for the license you specified. :(\n"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    print("\nIn order to verify your eligibility,\n\
I would need the full name of the state of issuance, the name of the license, and your age.")
    time.sleep(1)
    # initialize answer
    ans = ''

    # ensure user types in valid input
    while True:
        ans = input("\nWould you like to proceed? Type y or n: ")
        if ans == formatted('y') or ans == formatted('YES') or ans == formatted('NO') or ans == formatted('n'):
            break


    if ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes' or ans == 'YES':
        print('Thank you.')
        time.sleep(1)

        # initialize variables
        state = ''
        license = ''

        # Ensure state field is not left blank
        while True:
            state = input("Which state are you from? ")
            if is_state(state) is not None:
                break
            else:
                print('\nInvalid state. Confirm that the spelling is correct.\n')

        # ensure license field is not left blank
        while True:
            license = input("What license do you intend to get?\t a. Full?\t b.  Provisional?\t c. Learner's Permit? \nType a, b or c: ")
            if is_license(license) is not None:
                break
            else:
                print('\nInvalid license. Confirm that the spelling is correct.\n')

        # ensure age is not left blank
        while True:
            try:
                age = int(input("How old are you? "))
                if age > 0:
                    break
            except ValueError:
                print('\nInvalid age\n')

        # verify eligbility
        print(Eligibility(state, license, age))

    else:
        print('Thank you for yor response but unfortunately I cannot help without the information. If you do change your mind, just run me again. Have a good day!')
   


# REFERENCES:
# World Population Review(2021). Driving Age By State 2021. https://worldpopulationreview.com/state-rankings/driving-age-by-state