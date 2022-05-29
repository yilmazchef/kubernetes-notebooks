import imp
import os
import runpy
import sys
import time
import pip
import watchdog.events
import watchdog.observers
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength
from folder_manager import filter_files
from docx_manager import to_docx, add_header, add_footer
from pptx_manager import to_pptx


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.md'],
                                                             ignore_directories=True, case_sensitive=False)
        print(sys.getdefaultencoding())

    def on_created(self, event):
        print(f"{event.src_path} is created.")
        # Event is created, you can process it now

    def on_modified(self, event):
        print(f"Other document formats for {event.src_path} are being autogenerated.")
        sync(event.src_path)

    def on_deleted(self, event):
        os.remove(event.src_path.replace(".md", "docx"))


def sync(source_file: str) -> tuple:

    pBarMax = 2
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pBar = ProgressBar(widgets=widgets, maxval=pBarMax)

    pBar.start()
    pBarCount = 0

    docx_file = to_docx(source_file)

    header_image = os.getcwd() + os.path.sep + "Service" + \
        os.path.sep + "header.png"
    header_text = open(os.getcwd() + os.path.sep +
                       "Service" + os.path.sep + "header.txt", "r")
    add_header(docx_file, header_image, header_text)

    footer_image = os.getcwd() + os.path.sep + "Service" + \
        os.path.sep + "footer.png"
    footer_text = open(os.getcwd() + os.path.sep +
                       "Service" + os.path.sep + "footer.txt", "r")
    add_footer(docx_file, footer_image, footer_text)

    pBarCount += 1
    pBar.update(pBarCount)

    pptx_file = to_pptx(source_file)

    pBarCount += 1
    pBar.update(pBarCount)

    pBar.finish()

    return docx_file, pptx_file


if __name__ == "__main__":

    src_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
