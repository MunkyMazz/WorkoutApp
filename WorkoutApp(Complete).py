import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

# Helper function to calculate BMI and return category
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    return bmi, category

# UserInfo, WorkoutPlanner, DietTips classes unchanged from your snippet
class UserInfo:
    def __init__(self):
        self.height = None
        self.weight = None
        self.gender = None
        self.eating_habits = None
        self.weight_goal = None
        self.body_type = None
        self.body_type_image = None
        self.workout_days = None
        self.workout_time = None
        self.food_allergies = None
        self.sicknesses = None
        self.fitness_level = None
        self.fitness_goal = None

class WorkoutPlanner:
    def __init__(self, user_info):
        self.user_info = user_info
        self.workout_plans = {
            "Beginner": {
                "Lose Weight": {
                    "Push Day": [
                        "Bench Press: 3 sets of 10 reps (moderate weight, short rest)",
                        "Overhead Shoulder Press: 3 sets of 12 reps",
                        "Incline Dumbbell Press: 2 sets of 12 reps",
                        "Push-Ups: 2 sets of 15 reps",
                        "20 min brisk walking or cycling (cardio finisher)"
                    ],
                    "Pull Day": [
                        "Assisted Pull-Ups: 3 sets of 8 reps",
                        "Barbell Rows: 3 sets of 10 reps",
                        "Face Pulls: 2 sets of 15 reps",
                        "Dumbbell Bicep Curls: 2 sets of 12 reps",
                        "15 min jump rope or rowing (cardio finisher)"
                    ],
                    "Leg Day": [
                        "Goblet Squats: 3 sets of 12 reps",
                        "Romanian Deadlifts: 2 sets of 12 reps",
                        "Walking Lunges: 2 sets of 10 reps per leg",
                        "Calf Raises: 2 sets of 20 reps",
                        "20 min jogging or HIIT (cardio finisher)"
                    ]
                },
                "Build Muscles": {
                    "Push Day": [
                        "Bench Press: 3 sets of 8-10 reps (focus on progressive overload)",
                        "Overhead Shoulder Press: 3 sets of 10 reps",
                        "Tricep Dips (Assisted if needed): 2 sets of 8-10 reps",
                        "Incline Dumbbell Press: 2 sets of 10 reps",
                        "Push-Ups: 2 sets of 8-12 reps"
                    ],
                    "Pull Day": [
                        "Pull-Ups (Assisted if needed): 3 sets of 8 reps",
                        "Barbell Rows: 3 sets of 10 reps",
                        "Face Pulls: 2 sets of 12 reps",
                        "Dumbbell Bicep Curls: 2 sets of 10-12 reps",
                        "Seated Cable Rows: 3 sets of 10 reps"
                    ],
                    "Leg Day": [
                        "Goblet Squats: 3 sets of 10 reps",
                        "Romanian Deadlifts (RDL): 2 sets of 10 reps",
                        "Walking Lunges: 2 sets of 8 reps per leg",
                        "Calf Raises: 2 sets of 15 reps",
                        "Leg Extensions (Machine): 2 sets of 12 reps"
                    ]
                }
            },
            "Intermediate": {
                "Lose Weight": {
                    "Push Day": [
                        "Bench Press: 4 sets of 10 reps",
                        "Overhead Shoulder Press: 4 sets of 12 reps",
                        "Incline Dumbbell Press: 3 sets of 12 reps",
                        "Lateral Raises: 3 sets of 15 reps",
                        "20-30 min interval cardio"
                    ],
                    "Pull Day": [
                        "Pull-Ups: 4 sets of 8 reps",
                        "Barbell Rows: 4 sets of 10 reps",
                        "One-Arm Dumbbell Rows: 3 sets of 12 reps",
                        "Face Pulls: 3 sets of 15 reps",
                        "20 min HIIT on rowing machine"
                    ],
                    "Leg Day": [
                        "Squats: 4 sets of 10 reps",
                        "Romanian Deadlifts: 4 sets of 12 reps",
                        "Walking Lunges: 3 sets of 12 reps per leg",
                        "Calf Raises: 4 sets of 20 reps",
                        "25 min incline treadmill walk"
                    ]
                },
                "Build Muscles": {
                    "Push Day": [
                        "Bench Press: 4 sets of 8-12 reps",
                        "Overhead Shoulder Press: 4 sets of 8-10 reps",
                        "Incline Dumbbell Press: 3 sets of 10-12 reps",
                        "Tricep Dips: 3 sets of 10-12 reps",
                        "Lateral Raises: 3 sets of 12-15 reps",
                        "Cable Pushdowns: 3 sets of 12 reps"
                    ],
                    "Pull Day": [
                        "Pull-Ups: 4 sets of 8-10 reps",
                        "Barbell Rows: 4 sets of 8 reps",
                        "One-Arm Dumbbell Rows: 3 sets of 10 reps per arm",
                        "Face Pulls: 3 sets of 12-15 reps",
                        "Barbell or Dumbbell Bicep Curls: 3 sets of 10-12 reps",
                        "Hammer Curls: 3 sets of 12 reps"
                    ],
                    "Leg Day": [
                        "Squats (Barbell or Dumbbell): 4 sets of 8-12 reps",
                        "Romanian Deadlifts: 4 sets of 10-12 reps",
                        "Walking Lunges: 3 sets of 12 reps per leg",
                        "Leg Press: 3 sets of 10-12 reps",
                        "Calf Raises: 4 sets of 15-20 reps",
                        "Bulgarian Split Squats: 3 sets of 10 reps per leg"
                    ]
                }
            },
            "Advanced": {
                "Lose Weight": {
                    "Push Day": [
                        "Bench Press: 5 sets of 8 reps",
                        "Incline Dumbbell Press: 4 sets of 10 reps",
                        "Overhead Shoulder Press: 4 sets of 8 reps",
                        "Lateral Raises: 4 sets of 15 reps",
                        "30 min HIIT or cross-training"
                    ],
                    "Pull Day": [
                        "Weighted Pull-Ups: 5 sets of 6 reps",
                        "Barbell Rows: 5 sets of 8 reps",
                        "T-Bar Rows: 4 sets of 10 reps",
                        "Face Pulls: 4 sets of 15 reps",
                        "25 min running or rowing"
                    ],
                    "Leg Day": [
                        "Barbell Back Squats: 5 sets of 8 reps",
                        "Romanian Deadlifts: 5 sets of 10 reps",
                        "Walking Lunges: 4 sets of 12 reps per leg",
                        "Leg Press: 4 sets of 12 reps",
                        "30 min incline treadmill walk"
                    ]
                },
                "Build Muscles": {
                    "Push Day": [
                        "Bench Press (Heavy): 5 sets of 6-8 reps",
                        "Incline Dumbbell Press: 4 sets of 8-10 reps",
                        "Overhead Shoulder Press (Standing): 4 sets of 6-8 reps",
                        "Lateral Raises with Tempo Control: 4 sets of 12-15 reps",
                        "Tricep Dips (Weighted): 4 sets of 8-10 reps",
                        "Cable Flys: 3 sets of 12-15 reps"
                    ],
                    "Pull Day": [
                        "Weighted Pull-Ups: 5 sets of 6-8 reps",
                        "Barbell Rows: 5 sets of 8-10 reps",
                        "T-Bar Rows: 4 sets of 8-12 reps",
                        "Face Pulls with Rope: 4 sets of 12-15 reps",
                        "Preacher Curls (Barbell or Dumbbell): 4 sets of 10-12 reps",
                        "Hammer Curls: 4 sets of 12-15 reps",
                        "Deadlifts: 4 sets of 6 reps"
                    ],
                    "Leg Day": [
                        "Barbell Back Squats (Heavy): 5 sets of 6-8 reps",
                        "Romanian Deadlifts (RDL): 5 sets of 8-10 reps",
                        "Walking Lunges (Weighted): 4 sets of 12-15 reps per leg",
                        "Leg Press (High Volume): 4 sets of 10-12 reps",
                        "Calf Raises (Superset with Drop Sets): 5 sets of 20 reps",
                        "Bulgarian Split Squats (Weighted): 4 sets of 8 reps per leg"
                    ]
                }
            }
        }
        self.additional_tips = {
            "Beginner": [
                "Start with lighter weights to focus on form.",
                "Rest for 60-90 seconds between sets.",
                "Consistency is key – aim to complete all scheduled workouts.",
                "Hydrate well before, during, and after your workout."
            ],
            "Intermediate": [
                "Focus on progressive overload – increase weights each week.",
                "Incorporate compound movements for maximum muscle engagement.",
                "Maintain proper form to avoid injuries while lifting heavier.",
                "Add mobility exercises to improve range of motion."
            ],
            "Advanced": [
                "Utilize advanced techniques like drop sets and supersets.",
                "Increase workout intensity by reducing rest times.",
                "Periodize your training for continued progress.",
                "Incorporate recovery methods like foam rolling and stretching."
            ]
        }

    def generate_workout_plan(self):
        fitness_level = self.user_info.fitness_level
        fitness_goal = self.user_info.fitness_goal or "Build Muscles"
        plan = f"Workout Plan for {fitness_level} Level ({fitness_goal}):\n"
        if (
            fitness_level in self.workout_plans and
            fitness_goal in self.workout_plans[fitness_level]
        ):
            for day, exercises in self.workout_plans[fitness_level][fitness_goal].items():
                plan += f"\n{day}:\n"
                for exercise in exercises:
                    plan += f"- {exercise}\n"
            plan += "\nAdditional Tips:\n"
            for tip in self.additional_tips[fitness_level]:
                plan += f"- {tip}\n"
        else:
            plan += "General fitness exercises.\n"
        if self.user_info.sicknesses:
            plan += "\nNote: Adjust workout intensity as per doctor's advice.\n"
        return plan

class DietTips:
    def __init__(self, user_info):
        self.user_info = user_info

    def generate_tips(self, tips_type):
        tips = []
        if tips_type == "Simple Tips":
            tips = [
                "Drink at least 2 liters of water daily.",
                "Include a source of protein in every meal.",
                "Avoid processed foods and sugary drinks.",
                "Opt for whole grains instead of refined carbs."
            ]
        elif tips_type == "Detailed Daily Tips":
            tips = [
                "Day 1: Start with oatmeal and fruits. Lunch: Grilled chicken salad. Dinner: Steamed vegetables.",
                "Day 2: Breakfast: Smoothie with protein powder. Lunch: Tuna sandwich. Dinner: Grilled salmon and quinoa.",
                "Day 3: Breakfast: Eggs and avocado toast. Lunch: Stir-fried tofu. Dinner: Lentil soup.",
                "Day 4: Breakfast: Greek yogurt with nuts. Lunch: Turkey wrap with veggies. Dinner: Baked chicken and sweet potatoes."
            ]
        if self.user_info.food_allergies:
            allergy_warning = f": Avoid foods containing {self.user_info.food_allergies}."
            tips = [tip + allergy_warning for tip in tips]
        return tips

# Modified PlannerGUI with Save Workout Plan functionality
class PlannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Hard, Feel Better Workout Planner")
        self.root.configure(bg="#f2f2f2")
        self.user_info = UserInfo()
        self.generated_plan_data = None  # To store the generated plan for saving

        self.body_type_images = {
            "Slim": "./slim.png",
            "Shredded": "./shredded.png",
            "Muscular": "./muscular.png"
        }

        self.create_welcome_message()
        self.create_user_info_section()
        self.create_bmi_section()
        self.create_body_type_section()
        self.create_workout_preferences_section()
        self.create_health_section()
        self.create_fitness_level_section()
        self.create_tips_section()
        self.create_submit_button()
        self.create_save_button()   # Add Save button

    def create_welcome_message(self):
        tk.Label(
            self.root,
            text="Welcome to 'Work Hard, Feel Better' Workout Planner",
            font=("Arial", 16, "bold"),
            bg="#f2f2f2"
        ).pack(pady=10)

    def create_user_info_section(self):
        self.user_info_frame = ttk.LabelFrame(self.root, text="User Information", padding="10")
        self.user_info_frame.pack(pady=10)

        tk.Label(self.user_info_frame, text="Height (cm):").grid(row=0, column=0, sticky="e", pady=5)
        self.height_entry = ttk.Entry(self.user_info_frame)
        self.height_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.user_info_frame, text="Weight (kg):").grid(row=1, column=0, sticky="e", pady=5)
        self.weight_entry = ttk.Entry(self.user_info_frame)
        self.weight_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.user_info_frame, text="Gender:").grid(row=2, column=0, sticky="e", pady=5)
        self.gender = ttk.Combobox(self.user_info_frame, values=["Male", "Female", "Other"])
        self.gender.grid(row=2, column=1, pady=5)

        tk.Label(self.user_info_frame, text="Eating Habits:").grid(row=3, column=0, sticky="e", pady=5)
        self.eating_habits = ttk.Combobox(self.user_info_frame, values=["Healthy", "Moderate", "Unhealthy"])
        self.eating_habits.grid(row=3, column=1, pady=5)

    # BMI Calculator Section
    def create_bmi_section(self):
        self.bmi_frame = ttk.LabelFrame(self.root, text="BMI Calculator", padding="10")
        self.bmi_frame.pack(pady=10)

        ttk.Button(self.bmi_frame, text="Calculate BMI", command=self.calculate_bmi_action).grid(row=0, column=0, padx=5)
        self.bmi_result_label = ttk.Label(self.bmi_frame, text="(Enter height and weight above, then click)")
        self.bmi_result_label.grid(row=0, column=1, padx=5)

    def calculate_bmi_action(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi, bmi_category = calculate_bmi(weight, height)
            msg = f"Your BMI: {bmi} ({bmi_category})"
            self.bmi_result_label.config(text=msg)
        except Exception:
            self.bmi_result_label.config(text="Please enter valid height/weight.")

    def create_body_type_section(self):
        self.body_frame = ttk.LabelFrame(self.root, text="Body Type and Goal", padding="10")
        self.body_frame.pack(pady=10)

        tk.Label(self.body_frame, text="Desired Weight Goal (kg):").grid(row=0, column=0, sticky="e", pady=5)
        self.weight_goal_entry = ttk.Entry(self.body_frame)
        self.weight_goal_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.body_frame, text="Body Type:").grid(row=1, column=0, sticky="e", pady=5)
        self.body_type = ttk.Combobox(self.body_frame, values=["Slim", "Toned", "Muscular"])
        self.body_type.grid(row=1, column=1, pady=5)

    def create_workout_preferences_section(self):
        self.workout_frame = ttk.LabelFrame(self.root, text="Workout Preferences", padding="10")
        self.workout_frame.pack(pady=10)

        tk.Label(self.workout_frame, text="Workout Days (e.g., Mon, Wed, Fri):").grid(row=0, column=0, sticky="e", pady=5)
        self.workout_days_entry = ttk.Entry(self.workout_frame)
        self.workout_days_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.workout_frame, text="Workout Time (minutes/day):").grid(row=1, column=0, sticky="e", pady=5)
        self.workout_time_entry = ttk.Entry(self.workout_frame)
        self.workout_time_entry.grid(row=1, column=1, pady=5)

    def create_health_section(self):
        self.health_frame = ttk.LabelFrame(self.root, text="Health Information", padding="10")
        self.health_frame.pack(pady=10)

        tk.Label(self.health_frame, text="Food Allergies (comma-separated):").grid(row=0, column=0, sticky="e", pady=5)
        self.food_allergies_entry = ttk.Entry(self.health_frame)
        self.food_allergies_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.health_frame, text="Sicknesses:").grid(row=1, column=0, sticky="e", pady=5)
        self.sicknesses_entry = ttk.Entry(self.health_frame)
        self.sicknesses_entry.grid(row=1, column=1, pady=5)

    def create_fitness_level_section(self):
        self.fitness_level_frame = ttk.LabelFrame(self.root, text="Fitness Level", padding="10")
        self.fitness_level_frame.pack(pady=10)

        tk.Label(self.fitness_level_frame, text="Fitness Level:").grid(row=0, column=0, sticky="e", pady=5)
        self.fitness_level = ttk.Combobox(self.fitness_level_frame, values=["Beginner", "Intermediate", "Advanced"])
        self.fitness_level.grid(row=0, column=1, pady=5)

    def create_tips_section(self):
        tk.Label(self.root, text="Choose Tips Type:", bg="#f2f2f2").pack(pady=5)
        self.tips_choice = ttk.Combobox(self.root, values=["Simple Tips", "Detailed Daily Tips"])
        self.tips_choice.pack()

    def create_submit_button(self):
        ttk.Button(self.root, text="Generate Plan", command=self.generate_plan).pack(pady=20)

    def create_save_button(self):
        self.save_btn = ttk.Button(self.root, text="Save Workout Plan", command=self.save_plan_to_file, state='disabled')
        self.save_btn.pack(pady=5)

    def generate_plan(self):
        try:
            self.user_info.height = int(self.height_entry.get())
            self.user_info.weight = int(self.weight_entry.get())
            self.user_info.gender = self.gender.get()
            self.user_info.weight_goal = int(self.weight_goal_entry.get())
            self.user_info.eating_habits = self.eating_habits.get()
            self.user_info.body_type = self.body_type.get()
            self.user_info.workout_days = self.workout_days_entry.get()
            self.user_info.workout_time = int(self.workout_time_entry.get())
            self.user_info.food_allergies = self.food_allergies_entry.get()
            self.user_info.sicknesses = self.sicknesses_entry.get()
            self.user_info.fitness_level = self.fitness_level.get()

            # Basic validation
            if not all([self.user_info.eating_habits, self.user_info.body_type, self.user_info.fitness_level]):
                raise ValueError("Please fill out all fields!")

            # BMI Calculation
            bmi, bmi_category = calculate_bmi(self.user_info.weight, self.user_info.height)
            bmi_msg = f"Your BMI is: {bmi} ({bmi_category})"

            # Use a dropdown for the fitness goal instead of a dialog
            goal_win = tk.Toplevel(self.root)
            goal_win.title("Select Fitness Goal")
            tk.Label(goal_win, text="What is your primary fitness goal?").pack(pady=10)
            goal_choice = ttk.Combobox(goal_win, values=["Lose Weight", "Build Muscles"])
            goal_choice.pack(pady=10)
            goal_choice.set("Lose Weight")
            def set_goal_and_continue():
                fitness_goal = goal_choice.get()
                if fitness_goal not in ("Lose Weight", "Build Muscles"):
                    messagebox.showerror("Input Error", "Please select a valid goal.")
                else:
                    self.user_info.fitness_goal = fitness_goal
                    goal_win.destroy()
                    self._finish_plan(bmi, bmi_category, bmi_msg)
            ttk.Button(goal_win, text="Continue", command=set_goal_and_continue).pack(pady=10)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def _finish_plan(self, bmi, bmi_category, bmi_msg):
        workout_planner = WorkoutPlanner(self.user_info)
        workout_plan = workout_planner.generate_workout_plan()
        diet_tips = DietTips(self.user_info).generate_tips(self.tips_choice.get())

        # Save plan data for later saving to a file
        self.generated_plan_data = {
            "User Info": vars(self.user_info),
            "BMI": {"value": bmi, "category": bmi_category},
            "Workout Plan": workout_plan,
            "Diet Tips": diet_tips
        }
        self.save_btn.config(state='normal')  # Enable the save button

        # Show generated plan (workout, diet, BMI)
        messagebox.showinfo(
            "Plan Generated", 
            f"{bmi_msg}\n\nYour workout and diet plan have been generated!\n\n{workout_plan}\nDiet Tips:\n" + "\n".join(diet_tips)
        )

    def save_plan_to_file(self):
        if self.generated_plan_data is None:
            messagebox.showwarning("No Plan", "Please generate a plan before saving!")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Save Workout Plan"
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    json.dump(self.generated_plan_data, file, indent=4)
                messagebox.showinfo("Saved", f"Workout plan saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlannerGUI(root)
    root.mainloop()
