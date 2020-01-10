from flask_wtf import FlaskFrom
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo,ValidationError
from application.models import Recipes


class GenerateIngredientsForm(FlaskForm): # Button to select random recipe ingredients and method 
    submit = SubmitField("Generate Recipe Idea")

class RecipeNameForm(FlaskForm): # Input for user to name a recipe
    recipe_name = StringField("Recipe Name",
    validators = [
        DataRequired(),
        Length(min= 2, max= 30)
    ]
    )

    subimit = SubmitField("Save Recipe")

    def validate_recipe_name(self,recipe_name):
        exists = bool(Recipes.query.filter_by(name = recipe_name.data).first())
        if exists:
            raise ValidationError("This recipe name already exists \n \
                Please choose a new name for the recipe")

class SearchForRecipe(FlaskForm):
    recipe_name = StringField("Recipe Name",
    validators = [
        DataRequired(),
        Length(min = 2, max = 30)
    ]
    )

    submit = SubmitField("Search")

    def validate_recipe_name(self,recipe_name):
        exists = bool(Recipes.query.filter_by(name = recipe_name.data).first())
        if not exists:
            raise ValidationError("This recipe does not yet exist")

