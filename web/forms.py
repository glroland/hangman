from django import forms

DIFFICULTY_CHOICES = (
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard")
)
class NewGameForm(forms.Form):
    difficulty_level = forms.ChoiceField(choices = DIFFICULTY_CHOICES, 
                                         label="Puzzle Difficulty:", 
                                         initial='', 
                                         widget=forms.Select(), 
                                         required=True)

    def getDifficultyLevel(self):
        return self.cleaned_data['difficulty_level']
