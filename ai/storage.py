from pipeline.storage import PipelineMixin
from require.storage import OptimizedFilesMixin
from django.contrib.staticfiles.storage import CachedStaticFilesStorage

class CachedPipelineRequireStorage(PipelineMixin, OptimizedFilesMixin, CachedStaticFilesStorage):
    pass