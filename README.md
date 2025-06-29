**Day 1:**
* .tar file is an archive (like .zip) which bundles multiple files into one. Does not compress them.
* .gz means GZIP compressed files
* GitHub is not optimized for large datasets (it will crash since it has a limit of 100MB/file).
    * use .gitignore to only track changes to code, not data.
* ls -a reveals hidden files
    * touch .gitignore creates a new empty file 

**Day 2:**
* When you unzipped the .tar files, especially the images, they got separated into subfolders based on hash prefixes
