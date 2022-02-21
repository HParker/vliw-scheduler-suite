make;
echo "- source order"
./vliwScheduler $1 4_wide_source_simple.s 0
echo "- critical path"
./vliwScheduler $1 4_wide_critpath_source_simple.s 1
echo "- resource order"
./vliwScheduler $1 4_wide_resource_source_simple.s 2
echo "- fanout"
./vliwScheduler $1 4_wide_fanout_source_simple.s 3
echo "- critical path resource tiebreaker"
./vliwScheduler $1 4_wide_critpath_resource_source_simple.s 4
echo "- critical path fanout tiebreaker"
./vliwScheduler $1 4_wide_critpath_fanout_source_simple.s 5
echo "- rename"
./vliwScheduler $1 4_wide_rename_source_simple.s 6
echo "done"
