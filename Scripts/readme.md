- Create World -
    Step 1: Ask OpenAI to generate a list of finished goods. Each good should have a category identifier. For instance, bread is food, sword is weapon. Export this list as a JSON file.
    Step 2: Ask OpenAI to generate a list of materials that comprises those finished goods, reusing materials as often as possible. If a material is made up of other materials, list that too. Export this in JSON.
    Step 3: Ask OpenAI to generate a list of population types and the finished good that they require in order to be happy. For instance, peasants need food. Nobles need luxury. Export this list as a JSON file.
    Step 4: Ask OpenAI to generate a list of settlements. A settlement has a list of populations broken down by population type, and has an array of resources that it produces each day.
