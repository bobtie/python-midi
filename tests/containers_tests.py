from unittest import *
import midi.containers
import midi.events


class ContainerTestCase(TestCase):

    def test_pattern_slice_tick_mode(self):


        a = midi.containers.Pattern()
        tr = midi.containers.Track()

        tr.append(midi.events.NoteOnEvent(pitch=60, tick=100))
        tr.append(midi.events.NoteOffEvent(pitch=60, tick=100))
        a.append(tr)
        a.make_ticks_abs()

        newa = a[:]

        self.assertEqual(a.tick_relative,newa.tick_relative)

        # evs = a[0][:]
        #
        # self.assertEqual(evs[0].tick,100)
        # self.assertEqual(evs[1].tick,200)


    def test_track_slice_tick_mode(self):

        tr = midi.containers.Track()

        tr.append(midi.events.NoteOnEvent(pitch=60, tick=100))
        tr.append(midi.events.NoteOffEvent(pitch=60, tick=100))
        tr.make_ticks_abs()

        newtr = tr[:]

        self.assertEqual(newtr.tick_relative,tr.tick_relative)

