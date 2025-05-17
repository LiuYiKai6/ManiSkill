import sapien.core as sapien

scene_config = sapien.SceneConfig()
engine = sapien.Engine()
scene = engine.create_scene(scene_config)
loader = scene.create_urdf_loader()
robot = loader.load("/home/robolab/yikailiu/ManiSkill/mani_skill/assets/robots/fetch/fetch.urdf")