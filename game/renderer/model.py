class RawModel(object):

    def __init__(self, vao_id, vtx_count):
        self._vao_id = vao_id
        self._vtx_count = vtx_count

    @property
    def vao_id(self):
        return self._vao_id

    @property
    def vertex_count(self):
        return int(self._vtx_count)
