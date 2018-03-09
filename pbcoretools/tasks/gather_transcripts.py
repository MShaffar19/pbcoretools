
import logging
import sys

from pbcommand.cli import pbparser_runner
from pbcommand.models import get_gather_pbparser, FileTypes
from pbcommand.utils import setup_log

from pbcoretools.chunking.gather import run_main_gather_transcripts

log = logging.getLogger(__name__)


class Constants(object):
    TOOL_ID = "pbcoretools.tasks.gather_transcripts"
    CHUNK_KEY = "$chunk:transcriptset_id"
    VERSION = "0.1.0"
    DRIVER = "python -m pbcoretools.tasks.gather_transcripts --resolved-tool-contract "


def get_parser():
    p = get_gather_pbparser(Constants.TOOL_ID,
                            Constants.VERSION,
                            "TranscriptSet Gather",
                            "General Chunk Transcript Gather",
                            Constants.DRIVER,
                            is_distributed=True)

    p.add_input_file_type(FileTypes.CHUNK, "cjson_in", "GCHUNK Json",
          "Gathered CHUNK Json with ConsensusAlignmentSet chunk key")

    p.add_output_file_type(FileTypes.DS_TRANSCRIPT,
                           "ds_out",
                           "TranscriptSet",
                           "Gathered TranscriptSet",
                           default_name="gathered")
    return p


def args_runner(args):
    return run_main_gather_transcripts(args.cjson_in,
                                       args.ds_out,
                                       args.chunk_key)


def rtc_runner(rtc):
    return run_main_gather_transcripts(rtc.task.input_files[0],
                                       rtc.task.output_files[0],
                                       rtc.task.chunk_key)


def main(argv=sys.argv):
    return pbparser_runner(argv[1:],
                           get_parser(),
                           args_runner,
                           rtc_runner,
                           log,
                           setup_log)


if __name__ == '__main__':
    sys.exit(main())
