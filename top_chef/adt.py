class TopChefException(Exception):
    pass

#  Structure to hold a chef
class Chef:
    def __init__(self, chef_id=None, chef_name=None, chef_restaurant=None):
        self.id = chef_id
        self.name = chef_name
        self.restaurant = chef_restaurant
        self.score = 0.0

    def get_id(self):
        return self.id

    def add_score(self, score):
        self.score += score

    def get_name(self):
        return self.name

    def get_restaurant(self):
        return self.restaurant

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        chef_str = "ID: %s; " % (str(self.id))
        chef_str += "NAME: %s; " % (self.name)
        chef_str += "RESTAURANT: %s; " % (self.restaurant)
        chef_str += "SCORE: %s" % (self.score)
        return chef_str

# Structure to hold all chefs
class Chefs:
    def __init__(self):
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        if id in self.chefs:
            return True

        return False

    def get_ids(self):
        chefsIds = []
        for id in self.chefs:
            chefsIds.append(id)
        return chefsIds

    def add_chef(self, name, restaurant):
        if len(self.chefs) == 0: # Si no hay ningún Chef añadido, ese Chef será el primero y por tanto la ID será 1.
            id = 1
        else:
            for chefID in self.chefs: # Para generar la ID que toca, vamos al último Chef de la lista y le sumamos uno a su ID.
                continue
            id = chefID+1
        NewChef = Chef(id, name, restaurant) # Una vez se tienen los datos necesarios, creamos un objeto de la clase Chef.
        self.chefs[id] = NewChef # Añadimos el Chef en el diccionario, la clave es la ID y el valor el Chef como objeto.

        return NewChef

    def get_chef(self, id):
        chef = self.chefs[id]
        return chef

    def is_sorted(self):
        if len(self.sorted_chefs) == 0 or len(self.sorted_chefs) == 1: # Si la lista está vacía o solo hay un elemento, podemos asegurar que está ordenada.
            return True
        else:
            loop = 0
            while loop != len(self.sorted_chefs)-1: # Vamos a recorrer la lista y comparar un elemento con su siguiente, si vemos que el incial tiene una puntuación menor que el siguiente, podemos asegurar que no está ordenada.
                if (self.sorted_chefs[loop]).score < (self.sorted_chefs[loop+1]).score:
                    return False
                loop += 1
            return True # Si llegamos aquí, no se ha hecho el 'Return', por tanto la lista está ordenada.

    def sort_chefs(self):
        for chefObject in self.chefs.values():
            self.sorted_chefs.append(chefObject) # Primero añadimos los elementos a la lista sin ordenar.

        for chefPosition in range (1, len(self.sorted_chefs)): # Aplicamos el algoritmo InsertionSort.
            actualChef = self.sorted_chefs[chefPosition]
            while chefPosition > 0 and (self.sorted_chefs[chefPosition - 1]).score < actualChef.score:
                self.sorted_chefs[chefPosition] = self.sorted_chefs[chefPosition - 1]
                chefPosition -= 1
                self.sorted_chefs[chefPosition] = actualChef

        return self.sorted_chefs

    def get_top_n(self, n=1):
        topChefs = []
        for i in range (n): # Como aquí ya tenemos la lista ordenada, simplemente recorremos esa lista elemento a elemento, tantas veces como se nos pida.
            chef = self.sorted_chefs[i]
            topChefs.append(chef)
        return topChefs

    def __str__(self):
        chefs_str = ""
        for chef in self.chefs.values:
            chefs_str += str(chef)
            chefs_str += str("\n")

        return chefs_str

    def __len__(self):
        len = len(self.chefs)
        return len

# Structure to hold a recipe
class Recipe:
    def __init__(self, rec_id=None, rec_name=None, rec_chef_id=None):
        self.id = rec_id
        self.name = rec_name
        self.chef_id = rec_chef_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score

    def get_chef_id(self):
        return self.chef_id

    def __str__(self):
        rec_str = "ID: %s; " % (str(self.id))
        rec_str += "NAME: %s; " % (self.name)
        rec_str += "CHEF ID: %s; " % (self.chef_id)
        rec_str += "SCORE: %s" % (self.score)
        return rec_str

# Structure to hold the recipes
class Recipes:
    def __init__(self): # Funciona exactamente igual que la clase 'Chefs'.
        self.recipes = {}
        self.next_recipe = 0
        self.sorted_recipes = []

    def add_recipe(self, chef_id, name):
        if len(self.recipes) == 0:
            id = 1
        else:
            for recipeID in self.recipes:
                continue
            id = recipeID+1

        NewRecipe = Recipe(id, name, chef_id)
        self.recipes[id] = NewRecipe
        return NewRecipe

    def get_ids(self):
        recipeIds = []
        for recipeId in self.recipes:
            recipeIds.append(recipeId)
        return recipeIds

    def exists(self, id):
        if id in self.recipes:
            return True
        return False

    def get_recipe(self, recipe_id):
        recipe = self.recipes[recipe_id]
        return recipe

    def is_sorted(self):
        if len(self.sorted_recipes) == 0 or len(self.sorted_recipes) == 1:
            return True
        else:
            loop = 0
            while loop != len(self.sorted_recipes)-1:
                if (self.sorted_recipes[loop]).score < (self.sorted_recipes[loop+1]).score:
                    return False
                loop += 1
            return True

    def sort_recipes(self):
        for recipeObject in self.recipes.values():
            self.sorted_recipes.append(recipeObject)

        for recipePosition in range (1, len(self.sorted_recipes)):
            actualRecipe = self.sorted_recipes[recipePosition]
            while recipePosition > 0 and (self.sorted_recipes[recipePosition - 1]).score < actualRecipe.score:
                self.sorted_recipes[recipePosition] = self.sorted_recipes[recipePosition - 1]
                recipePosition -= 1
                self.sorted_recipes[recipePosition] = actualRecipe

        return self.sorted_recipes

    def get_top_n(self, n=1):
        topRecipes = []
        for i in range (n):
            recipe = self.sorted_recipes[i]
            topRecipes.append(recipe)
        return topRecipes

    def __str__(self):
        recipes_str = ""
        for recipe in self.recipes.values:
            recipes_str += str(recipe)
            recipes_str += str("\n")

        return recipes_str

    def __len__(self):
        len = len(self.recipes)
        return len

# Structure to hold a review
class Review:
    def __init__(self, rev_id=None, review=None, rec_id=None):
        self.id = rev_id
        self.review = review
        self.recipe_id = rec_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_review(self):
        return self.review

    def get_recipe_id(self):
        return self.recipe_id

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        recipe_str = "ID: %s; " % (str(self.id))
        recipe_str += "REVIEW: %s; " % (self.review)
        recipe_str += "RECIPE ID: %s; " % (self.recipe_id)
        recipe_str += "SCORE: %s" % (self.score)
        return recipe_str

# Structure to hold the reviews
class Reviews:
    def __init__(self): # Funciona exactamente igual que la clase 'Chefs'.
        self.reviews = {}
        self.next_review = 0
        self.sorted_reviews = []

    def add_review(self, rec_id, review):
        if len(self.reviews) == 0:
            id = 1
        else:
            for reviewID in self.reviews:
                continue
            id = reviewID + 1

        NewReview = Review(id, review, rec_id)
        self.reviews[id] = NewReview
        return NewReview

    def get_ids(self):
        reviewIds = []
        for reviewId in self.reviews:
            reviewIds.append(reviewId)
        return reviewIds

    def exists(self, id):
        if id in self.reviews:
            return True
        return False

    def get_review(self,rev_id):
        review = self.reviews[rev_id]
        return review

    def min_score(self):
        minReview = None
        for review in self.reviews.values():
            try:
                if review.score < minReview.score:
                    minReview = review
            except:
                minReview = review
        return minReview.score


    def max_score(self):
        maxReview = None
        for review in self.reviews.values():
            try:
                if review.score > maxReview.score:
                    maxReview = review
            except:
                maxReview = review
        return maxReview.score

    def is_sorted(self):
        if len(self.sorted_reviews) == 0 or len(self.sorted_reviews) == 1:
            return True
        else:
            loop = 0
            while loop != len(self.sorted_reviews)-1:
                if (self.sorted_reviews[loop]).score < (self.sorted_reviews[loop+1]).score:
                    return False
                loop += 1
            return True


    def sort_reviews(self):
        for recipeReview in self.reviews.values():
            self.sorted_reviews.append(recipeReview)

        for reviewPosition in range (1, len(self.sorted_reviews)):
            actualReview = self.sorted_reviews[reviewPosition]
            while reviewPosition > 0 and (self.sorted_reviews[reviewPosition - 1]).score < actualReview.score:
                self.sorted_reviews[reviewPosition] = self.sorted_reviews[reviewPosition - 1]
                reviewPosition -= 1
                self.sorted_reviews[reviewPosition] = actualReview

        return self.sorted_reviews

    def get_top_n(self, n=1):
        topReview = []
        for i in range (n):
            review = self.sorted_reviews[i]
            topReview.append(review)
        return topReview

    def __str__(self):
        rev_str = ""
        for review in self.reviews.values():
            rev_str += str(review)
            rev_str += ("\n")
        return rev_str


class TopChef:

    def __init__(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        chefs = self.chefs
        recipes = self.recipes
        reviews = self.reviews
        dataFile = open(path, "r") # Abrimos el archivo que contiene los Chefs, Recetas y Reviews.
        for fileLine in dataFile: # Recorremos el archivo línea a línea.
            fileLine = fileLine.replace("\n","") # Eliminamos si hay un salto de línea.
            fileContent = fileLine.split("\t") # Separamos los elementos de cada línea mediante la tabulación.
            if fileContent[0] == "CHEF": # Si tenemos un Chef, crearemos un objeto de esa clase con la información que nos ha dado el archivo.
                chefs.add_chef(fileContent[1], fileContent[2])
                chefsIds = chefs.get_ids()
                chefId = chefsIds[-1] # Guardamos la ID de ese chef para asociar luego sus recetas.
            elif fileContent[0] == "COURSE": # Si tenemos una receta, crearemos un objeto de esa clase con la información que nos ha dado el archivo.
                recipes.add_recipe(chefId, fileContent[1])
                recipesIds = recipes.get_ids()
                recipeId = recipesIds[-1] # Guardamos la ID de esa receta para asociar luego sus reviews.
            else:
                reviews.add_review(recipeId, fileContent[0]) # Si no nos indica nada, es una review.
        dataFile.close()

    def clear(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def add_chef(self, name, rest):
        return self.chefs.add_chef(name, rest)

    def add_recipe(self, id_chef, name):
        return self.recipes.add_recipe(id_chef, name)

    def add_review(self, id_rev,review):
        return self.reviews.add_review(id_rev, review)

    def compute_scores(self, word_dict):
        self.compute_reviews_score(word_dict)
        self.compute_recipes_score()
        self.compute_chefs_score()

    def compute_reviews_score(self, word_dict):
        for rev_id in self.reviews.get_ids(): # Vamos a ir obteniendo todas las reviews.
            review = self.reviews.get_review(rev_id)
            reviewString = review.review
            reviewString = reviewString.split(" ") # Queremos analizar las palabras de esa review, por tanto añadimos cada palabra en la lista.
            for reviewWord in reviewString: # Recorreremos cada palabra para eliminar si hay algún signo de puntuación, y transformar a minúsculas.
                reviewWord = reviewWord.replace(",", "")
                reviewWord = reviewWord.replace(".", "")
                reviewWord = reviewWord.replace(";", "")
                reviewWord = reviewWord.replace("!", "")
                reviewWord = reviewWord.replace("?", "")
                reviewWord = reviewWord.lower()
                if reviewWord in word_dict.get_words(): # Si esa palabra está en el diccionario de palabras, buscamos la puntuación de esa palabra y se la añadimos a la review.
                    addingScore = word_dict.get_value(reviewWord)
                    review.score += addingScore

        self.normalize_reviews_scores() # Vamos a normalizar las puntuaciones de cada review.

    def normalize_reviews_scores(self):
        minRawScore = self.reviews.min_score()
        maxRawScore = self.reviews.max_score()
        allReviews = self.reviews
        reviewsIds = allReviews.get_ids()

        for reviewId in reviewsIds: # Recorremos cada review y calculamos su puntuación normalizada, y la substituïmos por la antigua.
            actualReview = allReviews.get_review(reviewId)
            rawScore = actualReview.score
            normScore = (rawScore - minRawScore) / (maxRawScore - minRawScore)
            actualReview.score = normScore


    def compute_recipes_score(self):
        allReviews = []
        for rev_id in self.reviews.get_ids():
            review = self.reviews.get_review(rev_id)
            allReviews.append(review)

        recipeIds = self.recipes.get_ids()
        for recipeId in recipeIds:
            recipe = self.recipes.get_recipe(recipeId)
            actualRecipeScores = []
            actualRecipeId = recipe.id

            for review in allReviews:
                if review.recipe_id == actualRecipeId:
                    actualRecipeScores.append(review.score)

            l = len(actualRecipeScores)
            if l != 0:  # Evitamos una división entre 0.
                normalizedScore = 0
                for score in actualRecipeScores:
                    normalizedScore += score
                finalScore = normalizedScore / l
                recipe.add_score(finalScore)

        self.normalize_recipes_scores()

    def normalize_recipes_scores(self):
        recipeIds = self.recipes.get_ids()
        maxRawScore = None
        minRawScore = None
        for recipeId in recipeIds:
            recipe = self.recipes.get_recipe(recipeId)
            try:
                if recipe.score > maxRawScore:
                    maxRawScore = recipe.score
                if recipe.score < minRawScore:
                    minRawScore = recipe.score
            except:
                maxRawScore = recipe.score
                minRawScore = recipe.score

        for recipeId in recipeIds:
            recipe = self.recipes.get_recipe(recipeId)
            rawScore = recipe.score
            normScore = (rawScore - minRawScore) / (maxRawScore - minRawScore)

    def compute_chefs_score(self):
        allRecipes = []
        for rec_id in self.recipes.get_ids():
            recipe = self.recipes.get_recipe(rec_id)
            allRecipes.append(recipe)

        chefIds = self.chefs.get_ids()
        for chefId in chefIds:
            chef = self.chefs.get_chef(chefId)
            actualChefScores = []
            actualChefId = chef.id

            for recipe in allRecipes:
                if recipe.chef_id == actualChefId:
                    actualChefScores.append(recipe.score)

            l = len(actualChefScores)
            if l != 0:
                normalizedScore = 0
                for score in actualChefScores:
                    normalizedScore += score
                finalScore = normalizedScore / l
                chef.add_score(finalScore)


    def normalize_chefs_scores(self):
        chefIds = self.chefs.get_ids()
        maxRawScore = None
        minRawScore = None
        for chefId in chefIds:
            chef = self.chefs.get_chef(chefId)
            try:
                if chef.score > maxRawScore:
                    maxRawScore = chef.score
                if chef.score < minRawScore:
                    minRawScore = chef.score
            except:
                maxRawScore = chef.score
                minRawScore = chef.score

    def sort_structures(self):
        self.chefs.sort_chefs()
        self.recipes.sort_recipes()
        self.reviews.sort_reviews()

    def get_top_n_chefs(self, n=1):
        try:
            if self.chefs.is_sorted():
                nChefs = self.chefs.get_top_n(n)
            else:
                self.sort_structures()
                nChefs = self.chefs.get_top_n(n)
            return nChefs

        except IndexError:
            return False

    def get_top_n_recipes(self, n=1):
        try:
            if self.recipes.is_sorted():
                nRecipes = self.recipes.get_top_n(n)
            else:
                self.sort_structures()
                nRecipes = self.recipes.get_top_n(n)
            return nRecipes

        except IndexError:
            return False

    def get_top_n_reviews(self, n=1):
        try:
            if self.reviews.is_sorted():
                nReviews = self.recipes.get_top_n(n)
            else:
                self.sort_structures()
                nReviews = self.reviews.get_top_n(n)
            return nReviews

        except IndexError:
            return False

    def show_chefs(self, chefs):
        if not chefs:
            print("Wrong input!")
        else:
            for chef in chefs:
                print(chef)

    def show_recipes(self, recipes):
        if not recipes:
            print("Wrong input!")
        else:
            for recipe in recipes:
                print(recipe)

    def show_reviews(self, reviews):
        if not reviews:
            print("Wrong input!")
        else:
            for review in reviews:
                print(review)
