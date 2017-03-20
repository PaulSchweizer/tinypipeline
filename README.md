[![Build Status](https://travis-ci.org/PaulSchweizer/tinypipeline.svg?branch=master)](https://travis-ci.org/PaulSchweizer/tinypipeline) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/74303ae03455442ca6268a571ea824e8)](https://www.codacy.com/app/paulschweizer/tinypipeline?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PaulSchweizer/tinypipeline&amp;utm_campaign=Badge_Grade)

# tinypipeline
- A mini pipeline to handle personal projects
- It's based on the file system

# Folder Structure
    ProjectsRoot
        ProjectName

          .tinypipeline.project
              {"description": "A description ...", "template": "..."}

          _unsorted
            [Any unsorted or temporary material]

          maya
            ProjectName
              scenes
                AssetName
                  model
                    work
                      AssetName_model_work_v0001.ma
                    published
                      AssetName_model_v0001.ma
                      AssetName_model.ma (symlinked to latest version)
                  animation
                    ...

          photoshop
            _unsorted
              [Any random reference material]
            psd
              AssetName
                AssetName_v001.psd
            images
              [exported images]

          python
            python_module
              python_module.py

          unity
            ProjectName
              Assets
                cs
                  script.cs
                fbx
                  AssetName_model.fbx
                prefab
                  Prefab.prefab
