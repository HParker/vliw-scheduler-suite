#! /usr/bin/ruby

COMPILER = ARGV[0] || "/home/vagrant/vex-3.43/bin/cc"

control = ARGV[1] || "simple.s"
control_program_name = "simple"

file_names = [
    "4_wide_source_simple.s",
    "4_wide_critpath_source_simple.s",
    "4_wide_resource_source_simple.s",
    "4_wide_fanout_source_simple.s",
    "4_wide_critpath_resource_source_simple.s",
    "4_wide_critpath_fanout_source_simple.s",
    "4_wide_rename_source_simple.s"
]

puts "#{COMPILER} -o #{control_program_name} #{control}"
status = system("#{COMPILER} -o #{control_program_name} #{control}")
unless status
    raise "Error compiling #{control}"
end

control_output = `./#{control_program_name} 1 2 3 4 5 6 7 8 9 10`

file_names.each do |fn|
    fn_progam_name = fn.gsub(".s", "")
    unless File.file?(fn)
        raise "File #{fn} missing!"
    end
    status = system("#{COMPILER} -o #{fn_progam_name} #{fn}")
    unless status
        raise "Error compiling #{fn}"
    end    

    test_output = `./#{fn_progam_name} 1 2 3 4 5 6 7 8 9 10`
    if test_output != control_output
        raise "#{fn_progam_name} didn't match control output\n+#{test_output}\n-#{control_output}"
    end
end

puts "SUCCESS!"