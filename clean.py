import os
import glob

def cleanLatexArtifacts():
    extensionsToDelete = [
        '*.aux',
        '*.fdb_latexmk', 
        '*.fls',
        '*.log',
        '*.synctex.gz'
    ]
    
    deletedFiles = []
    
    # Get all directories in current directory
    directories = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    
    for directory in directories:
        print(f"🔍 Cleaning {directory}")
        
        for extension in extensionsToDelete:
            pattern = os.path.join(directory, extension)
            files = glob.glob(pattern)
            
            for filePath in files:
                try:
                    os.remove(filePath)
                    deletedFiles.append(filePath)
                    print(f"  ✅ {filePath}")
                except Exception as e:
                    print(f"  ❌ Error: {filePath}")
    
    print(f"\n✨ Deleted {len(deletedFiles)} files")

if __name__ == "__main__":
    print("🧹 LaTeX Cleaner")
    print("=" * 20)
    cleanLatexArtifacts()
    print("✨ Done!")
