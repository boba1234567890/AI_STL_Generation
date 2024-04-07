import spacy
import random
import bpy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# User description of the object
user_description = "a car"

# Parse user description using spaCy
doc = nlp(user_description)

# Initialize parameters
length = 10  # default length
height = 5   # default height
engine_size = 3  # default engine size

# Interpret user description
for token in doc:
    if token.text == 'a':
        length *= 1.5
    elif token.text == 'car':
        height *= 1.5
    elif token.text == 'car':
        engine_size *= 1.5

# Generate base shape
bpy.ops.mesh.primitive_cube_add(size=length)
base_object = bpy.context.object

# Add tall rudder
bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=height)
rudder = bpy.context.object
rudder.location.x = length / 2  # Place rudder at the back of the object

# Add large wings with massive engines
bpy.ops.mesh.primitive_plane_add(size=length * 2)
wings = bpy.context.object
wings.location.y = length / 2  # Place wings on the sides of the object

# Add massive engines
for i in range(2):
    bpy.ops.mesh.primitive_cylinder_add(radius=engine_size, depth=1)
    engine = bpy.context.object
    engine.location.x = length / 2  # Place engines at the back of the object
    engine.location.y = (i - 0.5) * length  # Alternate sides

# Export to STL
bpy.ops.export_mesh.stl(filepath='generated_model2.stl')
