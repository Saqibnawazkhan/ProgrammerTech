import tkinter as tk
from tkinter import messagebox
import random


quiz_questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"], "answer": "Harper Lee"},
    {"question": "What is the smallest prime number?", "choices": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "What is the chemical symbol for water?", "choices": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
    {"question": "What is the largest planet in our solar system?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x500")
        self.root.configure(bg="#2C3E50")

        self.score = 0
        self.current_question = 0
        self.questions = random.sample(quiz_questions, len(quiz_questions))

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Quiz Game!", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="white")
        self.title_label.pack(pady=20)

        self.rules_label = tk.Label(self.root, text="Answer the questions to the best of your ability.", font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.rules_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Helvetica", 14), command=self.start_quiz, bg="#1ABC9C", fg="white", relief="flat")
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.title_label.pack_forget()
        self.rules_label.pack_forget()
        self.start_button.pack_forget()

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label = tk.Label(self.root, text=question_data["question"], font=("Helvetica", 18), bg="#2C3E50", fg="white")
            self.question_label.pack(pady=20)

            self.choices_vars = [tk.BooleanVar() for _ in question_data["choices"]]

            self.choices_frame = tk.Frame(self.root, bg="#2C3E50")
            self.choices_frame.pack(pady=10)

            for i, choice in enumerate(question_data["choices"]):
                tk.Checkbutton(self.choices_frame, text=choice, variable=self.choices_vars[i], font=("Helvetica", 14), bg="#2C3E50", fg="white", selectcolor="#34495E", relief="flat").pack(anchor="w")

            self.submit_button = tk.Button(self.root, text="Submit Answer", font=("Helvetica", 14), command=self.check_answer, bg="#3498DB", fg="white", relief="flat")
            self.submit_button.pack(pady=20)
        else:
            self.show_results()

    def check_answer(self):
        selected_answers = [var.get() for var in self.choices_vars]
        selected_indices = [i for i, selected in enumerate(selected_answers) if selected]
        
        if len(selected_indices) == 1:
            selected_choice = self.questions[self.current_question]["choices"][selected_indices[0]]
            correct_answer = self.questions[self.current_question]["answer"]
            
            if selected_choice == correct_answer:
                self.score += 1
                messagebox.showinfo("Correct", "Correct answer!")
            else:
                messagebox.showerror("Incorrect", f"Incorrect answer! The correct answer is: {correct_answer}")

            self.current_question += 1
            self.question_label.pack_forget()
            self.choices_frame.pack_forget()
            self.submit_button.pack_forget()

            self.show_question()
        else:
            messagebox.showwarning("Invalid Selection", "Please select exactly one answer.")

    def show_results(self):
        performance_message = self.get_performance_message()

        self.result_frame = tk.Frame(self.root, bg="#2C3E50")
        self.result_frame.pack(pady=20)

        self.result_label = tk.Label(self.result_frame, text=f"Your score: {self.score}/{len(self.questions)}", font=("Helvetica", 18), bg="#2C3E50", fg="white")
        self.result_label.pack(pady=10)

        self.performance_label = tk.Label(self.result_frame, text=performance_message, font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.performance_label.pack(pady=10)

        self.play_again_button = tk.Button(self.result_frame, text="Play Again", font=("Helvetica", 14), command=self.play_again, bg="#1ABC9C", fg="white", relief="flat")
        self.play_again_button.pack(pady=20)

    def get_performance_message(self):
        if self.score == len(self.questions):
            return "Excellent! You got all answers correct!"
        elif self.score >= len(self.questions) * 0.7:
            return "Great job! You scored well!"
        elif self.score >= len(self.questions) * 0.5:
            return "Good effort! You got more than half correct."
        else:
            return "Keep trying! You'll get better with practice."

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.questions = random.sample(quiz_questions, len(quiz_questions))

        self.result_frame.pack_forget()

        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
