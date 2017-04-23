from __future__ import print_function

from flowpipe.graph import Graph
from flowpipe.nodes.value_node import ValueNode

from tinypipeline.tools.flowpipe_nodes import io_nodes

from tinypipeline.tools.flowpipe_nodes import maya_nodes
reload(maya_nodes)

from tinypipeline.tools.flowpipe_nodes.environment_nodes import EnvNode
from tinypipeline.tools.flowpipe_nodes.object_nodes import AssetNode
from tinypipeline.tools.flowpipe_nodes.maya_nodes import CurrentAssetNode
from tinypipeline.tools.flowpipe_nodes.maya_nodes import SaveCurrentMayaSceneAs
from tinypipeline.tools.flowpipe_nodes.io_nodes import WriteTextToFileNode
from tinypipeline.tools.flowpipe_nodes.io_nodes import CopyFileNode


class AssetPublishFromCurrentScene(Graph):
    """Publish an Asset."""

    def __init__(self):
        super(AssetPublishFromCurrentScene, self).__init__('AssetPublish', list())
        current_asset = CurrentAssetNode()
        asset = AssetNode('Asset')
        current_asset.outputs['project'] >> asset.inputs['project']
        current_asset.outputs['name'] >> asset.inputs['name']
        current_asset.outputs['kind'] >> asset.inputs['kind']

        save_scene = SaveCurrentMayaSceneAs('SaveMayaFile')
        asset.outputs['next_version'] >> save_scene.inputs['file_path']

        notes = ValueNode('Notes', 'MyNotes')
        save_notes = WriteTextToFileNode('SaveNotes')
        notes.outputs['value'] >> save_notes.inputs['text']
        asset.outputs['next_version_notes'] >> save_notes.inputs['file_path']

        update_latest_scene = CopyFileNode('UpdateLatestScene')
        save_scene.outputs['file_path'] >> update_latest_scene.inputs['source']
        asset.outputs['latest_version'] >> update_latest_scene.inputs['destination']
        update_latest_notes = CopyFileNode('UpdateLatestText')
        save_notes.outputs['file_path'] >> update_latest_notes.inputs['source']
        asset.outputs['latest_version_notes'] >> update_latest_notes.inputs['destination']

        # unity_path = ValueNode('Unity', '/Unity/Test/Path/Assets')
        # copy_scene = CopyFileNode('CopyScene')

        # save_scene.outputs['file_path'] >> copy_scene.inputs['source']
        # unity_path.outputs['value'] >> copy_scene.inputs['destination']

        self.nodes = [current_asset, asset,
                      save_scene,
                      notes, save_notes,
                      update_latest_scene, update_latest_notes]
    # end def __init__
# end class AssetPublishFromCurrentScene


if __name__ == '__main__':
    graph = AssetPublishFromCurrentScene()
    graph.evaluate()
