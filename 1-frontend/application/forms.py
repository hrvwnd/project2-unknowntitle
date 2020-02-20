from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo,ValidationError
#from application.__init__ import LoginManager
#from flask_login import LoginManager, current_user
from application.models import Recipes, Users


class GenerateIngredientsForm(FlaskForm): # Button to select random recipe ingredients and method 
    submit = SubmitField("Generate Recipe Idea")


class RecipeNameForm(FlaskForm): # Input for user to name a recipe
    recipe_name = StringField("Recipe Name",
    validators = [
        DataRequired(),
        Length(min= 2, max= 30)
    ]
    )

    submit = SubmitField("Save Recipe")

    def validate_recipe_name(self,recipe_name):
        exists = bool(Recipes.query.filter_by(name = recipe_name.data).first())
        if exists:
            raise ValidationError("This recipe name already exists \n \
                Please choose a new name for the recipe")


class SearchForRecipe(FlaskForm):
    # Search for recipe Form
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
            raise ValidationError("This recipe does not exist")


class UpdateForm(FlaskForm):
    oldrecipe_name = StringField("Old Recipe Name",
    validators = [
        DataRequired(),
        Length(min = 2, max = 30)
    ]
    )

    recipe_name = StringField("New Recipe Name",
    validators = [
        DataRequired(),
        Length(min = 2, max = 30)
    ]
    )

    submit = SubmitField("Submit")

    def validate_oldrecipe_name(self,oldrecipe_name):
        exists = bool(Recipes.query.filter_by(name = oldrecipe_name.data).first())
        if not exists:
            raise ValidationError("This Recipe doesn't exist")

    def validate_recipe_name(self,recipe_name):
        exists = bool(Recipes.query.filter_by(name = recipe_name.data).first())
        if exists:
            raise ValidationError("This Recipe Name Already Exists")


class DeleteForm(FlaskForm):
    deleterecipe = StringField("Recipe to Delete",
    validators = [
        DataRequired(),
        Length(min = 2, max = 30)
    ]
    )
    deleteChoices = [(1,"Confirm"), (2,"Cancel")]
    confirmdelete = SelectField(u'Confirm Delete',
    choices = deleteChoices,
    default = 2, 
    validators = [
        DataRequired()
        ]
        )
    submit = SubmitField("Submit")
    
    def validate_confirmdelete(self, confirmdelete, deleteChoices):
        if confirmdelete.data not in deleteChoices:
            raise ValidationError("Not a Valid Choice")

    def validate_deleterecipe_name(self, deleterecipe):
        exists = bool(Recipes.query.filter_by(name = deleterecipe.data).first())
        if not exists:
            raise ValidationError("This Recipe doesn't exist")

# Account registration and Login
# Disabled for now
"""
class RegistrationForm(FlaskForm):
    username = StringField('User Name', 
    validators=[
        DataRequired(),
        Email()
        ]
        )
    password = PasswordField('Password',
    validators=[
        DataRequired()
        ]
        )
    confirm_password = PasswordField('Confirm Password',
    validators=[
        DataRequired(),
        EqualTo('password')
        ]
        )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Email is already in use!')
    """
"""
class LoginForm(FlaskForm):
    class LoginForm(FlaskForm):
    email = StringField('Email',
    validators = [
        DataRequired(),
        Email()
        ]
        )

    password = PasswordField('Password',
    validators = [
        DataRequired()
    ]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    """
