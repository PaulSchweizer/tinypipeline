"""Configuration values."""


env_vars = [
    # Current project
    'TINYPIPELINE_PROJECT'
]

root = 'C:/PROJECTS/'

padding = 4

maya_ext = 'ma'

patterns = {
    'project': '{project}',
    'project_config': '{project}/.tinypipeline.project.json',
    'unsorted': '{project}/_unsorted',
    'program': '{project}/{program}',
    'maya': '{project}/maya/{project}',
    'maya_subfolder': '{project}/maya/{project}/{folder}',
    'asset': '{project}/maya/{project}/scenes/{name}/{kind}',
    'step': '{project}/maya/{project}/scenes/{name}/{kind}/{step}',
    'asset_work': '{project}/maya/{project}/scenes/{name}/{kind}/work/{name}_{kind}_work_v{version}.{ext}',
    'notes': '{path}/.{filename}.notes',
    'asset_published': '{project}/maya/{project}/scenes/{name}/{kind}/published/{name}_{kind}_v{version}.{ext}',
    'asset_latest': '{project}/maya/{project}/scenes/{name}/{kind}/{name}_{kind}.{ext}'
}
