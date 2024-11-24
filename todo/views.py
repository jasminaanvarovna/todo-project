
from  django.shortcuts import HttpResponse

def task_create(request):
     html_response = """
     <!DOCTYPE html>
     <html lang="uz">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Yangi vazifa yaratish</title>
         <style>
             /* Asosiy body stilini sozlash */
             body {
                 font-family: Arial, sans-serif;
                 margin: 20px;
                 background-color: blue #f4f4f4;
                 color:  black #333;
             }

             h1 {
                 text-align: center;
             }

             /* Formani yaxshilash */
             form {
                 background-color: white;
                 padding: 20px;
                 border-radius: 8px;
                 box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                 max-width: 500px;
                 margin: 0 auto;
             }

             label {
                 display: block;
                 margin-bottom: 8px;
                 font-weight: bold;
             }

             input, textarea, select, button {
                 width: 100%;
                 padding: 10px;
                 margin-bottom: 12px;
                 border: 1px solid #ccc;
                 border-radius: 5px;
                 font-size: 16px;
             }

             textarea {
                 resize: vertical;
             }

             button {
                 background-color: #007bff;
                 color: white;
                 font-size: 16px;
                 cursor: pointer;
                 border: none;
             }

             button:hover {
                 background-color: #0056b3;
             }

             /* Responsive dizayn */
             @media (max-width: 600px) {
                 body {
                     margin: 10px;
                 }

                 form {
                     padding: 15px;
                 }
             }
         </style>
     </head>
     <body>
         <h1>Yangi vazifa yaratish</h1>
         <form action="#" method="post">
             <label for="vazifa-nomi">Vazifa nomi:</label>
             <input type="text" id="vazifa-nomi" name="vazifa-nomi" placeholder="Vazifa nomini kiriting" required>

             <label for="tavsif">Tavsif:</label>
             <textarea id="tavsif" name="tavsif" rows="4" placeholder="Vazifa tavsifini kiriting"></textarea>

             <label for="muddat">Muddati:</label>
             <input type="date" id="muddat" name="muddat" required>

             <label for="muhimlik-darajasi">Muhimlik darajasi:</label>
             <select id="muhimlik-darajasi" name="muhimlik-darajasi" required>
                 <option value="past">Past</option>
                 <option value="o'rta">O'rta</option>
                 <option value="yuqori">Yuqori</option>
             </select>

             <button type="submit">Vazifani saqlash</button>
         </form>
     </body>
     </html>
     

       """
     return HttpResponse(html_response)


