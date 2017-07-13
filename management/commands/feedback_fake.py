import random


from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

# Our custom provider inherits from the BaseProvider
class FeedbackTextProvider(BaseProvider):
    def opinion(self):
        opinion_list = [
            "Die mutherfuckers! Your product is shit!",
            "I did't like your pizza.",
            "I'm very happy.",
            "After sitting through hours of New Age rhetoric, I decided to have a crack at writing code to generate it automatically and speed things up a bit. I cobbled together a list of New Age buzzwords and cliché sentence patterns and this is the result.",
            "You may be ruled by turbulence without realizing it. Do not let it sabotage the deeper meaning of your myth. Dogma is the antithesis of self-actualization. Greed is born in the gap where serenity has been excluded.",
            "Reality has always been radiating pilgrims whose chakras are transformed into manna. We are at a crossroads of rejuvenation and dogma. Humankind has nothing to lose.",
            "Only a lifeform of the planet may foster this vision of faith. The complexity of the present time seems to demand a flowering of our souls if we are going to survive. You may be ruled by dogma without realizing it. Do not let it destroy the growth of your mission.",
        ]

        # We select a random destination from the list and return it
        return random.choice(opinion_list)

# Add the TravelProvider to our faker object
fake.add_provider(FeedbackTextProvider)

# We can now use the destination method:
print(fake.opinion())

def create_feedback():
    