import os

from tinypipeline.core.paths import Paths
from tinypipeline.tools.project_creator import ProjectCreator
from project_templates import base


def main(project):
    base.main(project)

    maya = Paths.maya(project=project)
    ProjectCreator.create_path(maya)

    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='cache'))
    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='data'))
    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='images'))
    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='renderData'))
    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='scenes'))
    ProjectCreator.create_path(Paths.maya_subfolder(project=project, folder='sourceimages'))

    with open(os.path.join(maya, 'workspace.mel'), 'w') as workspace:
        workspace.write("""
workspace -fr "fluidCache" "cache/nCache/fluid";
workspace -fr "JT_DC" "data";
workspace -fr "images" "images";
workspace -fr "CATIAV4_DC" "data";
workspace -fr "offlineEdit" "scenes/edits";
workspace -fr "STEP_DC" "data";
workspace -fr "furShadowMap" "renderData/fur/furShadowMap";
workspace -fr "SPF_DCE" "data";
workspace -fr "scripts" "scripts";
workspace -fr "CATIAV5_DC" "data";
workspace -fr "DAE_FBX" "data";
workspace -fr "shaders" "renderData/shaders";
workspace -fr "furFiles" "renderData/fur/furFiles";
workspace -fr "OBJ" "data";
workspace -fr "FBX export" "data";
workspace -fr "furEqualMap" "renderData/fur/furEqualMap";
workspace -fr "Autodesk Packet File" "data";
workspace -fr "DAE_FBX export" "data";
workspace -fr "SPF_DC" "data";
workspace -fr "movie" "movies";
workspace -fr "DXF_DCE" "data";
workspace -fr "move" "data";
workspace -fr "mayaAscii" "scenes";
workspace -fr "autoSave" "autosave";
workspace -fr "sound" "sound";
workspace -fr "mayaBinary" "scenes";
workspace -fr "ZPR_DCE" "data";
workspace -fr "STL_DCE" "data";
workspace -fr "iprImages" "renderData/iprImages";
workspace -fr "studioImport" "data";
workspace -fr "FBX" "data";
workspace -fr "DXF_DC" "data";
workspace -fr "UG_DCE" "data";
workspace -fr "renderData" "renderData";
workspace -fr "fileCache" "cache/nCache";
workspace -fr "eps" "data";
workspace -fr "3dPaintTextures" "sourceimages/3dPaintTextures";
workspace -fr "mel" "scripts";
workspace -fr "translatorData" "data";
workspace -fr "particles" "cache/particles";
workspace -fr "IV_DC" "data";
workspace -fr "scene" "scenes";
workspace -fr "DWG_DCE" "data";
workspace -fr "sourceImages" "sourceimages";
workspace -fr "clips" "clips";
workspace -fr "furImages" "renderData/fur/furImages";
workspace -fr "PTC_DC" "data";
workspace -fr "STL_DC" "data";
workspace -fr "IPT_DC" "data";
workspace -fr "CSB_DC" "data";
workspace -fr "SW_DC" "data";
workspace -fr "depth" "renderData/depth";
workspace -fr "audio" "sound";
workspace -fr "DWG_DC" "data";
workspace -fr "bifrostCache" "cache/bifrost";
workspace -fr "IGES_DCE" "data";
workspace -fr "Alembic" "data";
workspace -fr "illustrator" "data";
workspace -fr "diskCache" "data";
workspace -fr "UG_DC" "data";
workspace -fr "templates" "assets";
workspace -fr "OBJexport" "data";
workspace -fr "furAttrMap" "renderData/fur/furAttrMap";
workspace -fr "IGES_DC" "data";
                        """)