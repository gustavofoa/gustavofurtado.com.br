module.exports = function (grunt) {

  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-sitemap');

  grunt.initConfig({

    shell: {
      generate: {
        command: 'pelican content -s pelicanconf.py'
      }
    },

    watch: {
      files: [
        'content/*.md',
        'content/**/*.md',
        'theme/**/*.*',
        'pelicanconf.py',
        'content/static/*.*'
      ],
      tasks: ['build'],
      options: {
        livereload: 35729,
      }
    },

    sitemap: {
        dist: {
            homepage: 'http://www.gustavofurtado.com.br/',
            pattern: ['output/**/*.html', '!node_modules/**/*'],
            siteRoot: 'output/'
        }
    },

    connect: {
      server: {
        options: {
          port: 9001,
          livereload: 35729,
          base: 'output',
          hostname: 'localhost',
          open: true,
          debug: false
        }
      }
    },

    clean: {
      build: {
        src: ["output/*"]
      }
    }

  });

  grunt.registerTask('build', ['clean', 'shell:generate']);
  grunt.registerTask('serve', ['build', 'connect:server', 'watch']);
  grunt.registerTask('deploy', ['clean', 'less:main', 'shell:deploy']);

};
