<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stefan's Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="header">
    <a href="?page=home">Home</a>
    <a href="?page=projects">Projects</a>
    <a href="?page=about">About</a>
</div>

<?php
$page = $_GET['page'] ?? 'home';

switch ($page) {
    case 'projects':
        include 'projects.html';
        break;
    case 'about':
        include 'about.html';
        break;
    case 'home':
    default:
        include 'bookpage.html';
        
        // Add dynamic table
        echo "<div class='main'>";
        echo "<h2>Favorite Books</h2>";
        echo "<table>";
        echo "<tr><th>Title</th><th>Author</th><th>Genre</th></tr>";
        
        $books = [
            ["The Pragmatic Programmer", "Andrew Hunt", "Programming"],
            ["1984", "George Orwell", "Dystopian"],
            ["Clean Code", "Robert C. Martin", "Software Engineering"]
        ];

        foreach ($books as $book) {
            echo "<tr>";
            echo "<td>{$book[0]}</td><td>{$book[1]}</td><td>{$book[2]}</td>";
            echo "</tr>";
        }

        echo "</table>";
        echo "</div>";
        break;
}

include 'footer.html';
?>

</body>
</html>
