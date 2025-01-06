using System;

namespace ProgramLauncher
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Program Launcher!");
            Console.WriteLine("Type '1' to open Unity or '2' for VS Code:");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    OpenProgram(@"C:\Program Files\Unity\Editor\Unity.exe");
                    break;
                case "2":
                    OpenProgram(@"C:\Program Files\Microsoft VS Code\Code.exe");
                    break;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }

        static void OpenProgram(string programPath)
        {
            try
            {
                System.Diagnostics.Process.Start(programPath);
                Console.WriteLine($"Opened {programPath}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
